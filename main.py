import datetime
import hashlib
from fastapi import FastAPI, HTTPException
import requests
from flask import Response
import psycopg2
import os

app = FastAPI()
idx = 0
urls = {}

conn_str = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(conn_str)
    cursor = conn.cursor()
    cursor.execute("SELECT version();")

    record = cursor.fetchone()
    print("Database version:", record)

    cursor.close()
    conn.close()
except Exception as e:
    print("Error connecting to the database:", e)

@app.post("/shorten")
async def create_short_url(url: str):
    try:
        # url validation
        response = requests.get(url, timeout=5)
        if 200 <= response.status_code < 400:
            global idx, urls
            idx += 1
            code = hashlib.md5(url.encode()).hexdigest()
            code = code[:6]
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
            expiration_date = (datetime.datetime.now() + datetime.timedelta(days=69)).strftime("%Y-%m-%d %H:%M:%S %p")
            urls[code] = {
                    "id" : idx,
                    "short_code": code, # 'b7bf24'
                    "original_url": url,
                    "created_at": created_at, # 2021-09-01 12:00:00 PM
                    "last_updated_at": created_at,
                    "expiration_date": expiration_date,
                    "access_count": 0,
            }
            return urls[code]
        else:
            raise HTTPException(status_code=404, detail="Invalid URL")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=404, detail="An error occurred while validating the URL, please try again later")


@app.get("/shorten/{short_code}")
async def get_original_url(short_code: str):
    try:
        if short_code not in urls:
            raise HTTPException(status_code=404, detail="Short code not found")

        if urls[short_code]["expiration_date"] < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"):
            urls.pop(short_code)
            raise HTTPException(status_code=404, detail="Short code has expired")

        urls[short_code]["access_count"] += 1
        return urls[short_code]

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=404, detail="An error occurred while getting the original URL, please try again later")


@app.put("/shorten")
async def update_short_url(short_code: str, url: str):
    try:
        if short_code not in urls:
            raise HTTPException(status_code=404, detail="Short code not found")

        if urls[short_code]["expiration_date"] < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p"):
            urls.pop(short_code)
            raise HTTPException(status_code=404, detail="Short code has expired")

        urls[short_code]["original_url"] = url
        urls[short_code]["last_updated_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
        urls[short_code]["access_count"] = 0
        return urls[short_code]

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=404, detail="An error occurred while updating the short URL, please try again later")


@app.delete("/shorten/{short_code}")
async def delete_short_url(short_code: str):
    try:
        if short_code not in urls:
            raise HTTPException(status_code=404, detail="Short code not found")

        urls.pop(short_code)
        return Response(status=204, headers={"message": "Short URL deleted successfully"})

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=404, detail="An error occurred while deleting the short URL, please try again later")