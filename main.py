import datetime
from http.client import HTTPException
import hashlib
from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# You should create a RESTful API for a URL shortening service. The API should allow users to perform the following operations:
#
# Create a new short URL
# Retrieve an original URL from a short URL
# Update an existing short URL
# Delete an existing short URL
# Get statistics on the short URL (e.g., number of times accessed)
# You can optionally setup a minimal frontend to interact with the API and setup redirects for the short URLs to the original URLs.

idx = 0


@app.post("/shorten")
async def create_short_url(url: str):
    try:
        # url validation
        response = requests.get(url, timeout=5)
        if 200 <= response.status_code < 400:
            global idx
            idx += 1
            code = hashlib.md5(url.encode()).hexdigest()
            created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %p") # 2021-09-01 12:00:00 PM
            return {"id": idx,
                    "url": url,
                    "short_code": code[:6], # 'e62e24'
                    "createdAt" : created_at}
        else:
            raise HTTPException(status_code=404, detail="Invalid URL")
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=404, detail="An error occurred while validating the URL, please try again later")


@app.get("/shorten/{short_code}")
async def get_original_url(short_code: str):
    return {"short_code": short_code}