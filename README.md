# Simple HTTP Server in Python

Simple HTTP server written from scratch using Python sockets.

The project was created to better understand:
- TCP connections
- HTTP requests and responses
- routing
- static file serving
- unit testing with mocks

## Features

- Serving HTML/CSS/JS files
- Simple JSON API
- Custom HTTP response builder
- Basic routing system
- Error handling
- Docker support
- Unit tests

## Project structure

```text
handlers/     - request handlers
tests/        - unit and integration tests
website/      - static files
```

## Run locally

```bash
python server.py
```

## Run with Docker

```bash
docker compose up
```

## Example routes

Main HTML page
```text
/
```

Returns JSON response
```text
/api/v1/test
```

## Tests

```bash
pytest
```

## Reason

I wanted to better understand how HTTP servers work internally instead of only using frameworks like Flask or FastAPI.