import os

EXTERNAL_API_URL = os.getenv(
    "EXTERNAL_API_URL",
    "https://jsonplaceholder.typicode.com/posts"
)

API_KEY = os.getenv(
    "API_KEY",
    "demo-api-key"
)
