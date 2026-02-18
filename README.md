# \# Integration Gateway

# 

# A lightweight integration layer that simulates syncing customer data to an external SaaS API.

# 

# \## Features

# 

# \- REST endpoint for customer sync

# \- Payload transformation

# \- Header-based authentication

# \- Outbound API request handling

# \- Error handling with appropriate HTTP status codes

# \- Structured logging

# 

# \## Architecture

# 

# Client → Integration Gateway → External SaaS API

# 

# \## Run

# 

# pip install -r requirements.txt

# python app.py

# 

# \## Example Request

# 

# curl -X POST http://127.0.0.1:6000/sync-customer \\

# -H "Content-Type: application/json" \\

# -d "{\\"customer\_id\\":\\"789\\",\\"name\\":\\"Earl\\"}"

# 

# \## Example Response

# 

# {

# &nbsp; "status": "synced"

# }



