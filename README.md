# URL Shortener API

## Introduction

This project is a URL Shortener API built using FastAPI. The purpose of this project is to provide a practical example of integrating FastAPI with PostgreSQL, Redis, and other essential tools. It serves as a learning resource for those who want to deepen their understanding of backend development, database management, and API deployment.

## Features

- Shorten a given URL and generate a unique short code.
- Retrieve the original URL using the short code.
- Redirect to the original URL when the short code is accessed.
- Update the original URL associated with a short code.
- Delete a short code and its associated URL.
- Log and track the number of accesses to each URL.
- IP geolocation to log access locations.
- Caching with Redis to improve performance.
- Rate limiting to prevent abuse.
Learning Objective

The primary goal of this project is to facilitate learning and to gain a comprehensive understanding of network programming at a low level. By building the networking stack from the ground up, this project provides invaluable insights into the intricacies of network communication, socket programming, and error handling.

## Tech Stack

- **Python**: A high-level, interpreted programming language known for its simplicity and readability.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **PostgreSQL**: A powerful, open-source object-relational database system.
- **Redis**: An in-memory data structure store, used as a database, cache, and message broker.
- **Docker**: Used to containerize the application for easy deployment.

## Prerequisites

Before you start, make sure you have the following tools installed:

- Python 3.8+
- PostgreSQL
- Redis
- Docker (optional, for containerization)
- Git

## Getting Started

You can clone this repo and deploy it for free in Render foruse it as the backend of your URL shortener website.

API Endpoints

Here are the main endpoints for the API:

- `POST /shorten`: Shorten a new URL.
- `GET /shorten/{short_code}`: Retrieve the original URL using the short code.
- `PUT /shorten`: Update an existing short URL.
- `DELETE /shorten/{short_code}`: Delete a short URL.
- `GET /`: Redirect to the original URL using the short code.
- `GET /health`: Health check endpoint to ensure the API is running.

#### Manual Deployment

For manual deployment on a cloud server, you'll need to:

1. Set up the environment variables on your server.
2. Install PostgreSQL and Redis.
3. Run the FastAPI application with Uvicorn or Gunicorn.
4. Configure a reverse proxy like Nginx to handle incoming traffic.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.