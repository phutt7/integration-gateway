from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

EXTERNAL_API_URL = "https://jsonplaceholder.typicode.com/posts"
API_KEY = "demo-api-key"


@app.route("/sync-customer", methods=["POST"])
def sync_customer():
    data = request.json

    if not data or "customer_id" not in data:
        return jsonify({"error": "Invalid payload"}), 400

    # Transform incoming data
    transformed_payload = {
        "title": f"Customer {data['customer_id']}",
        "body": data.get("name", "Unknown"),
        "userId": 1
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(EXTERNAL_API_URL, json=transformed_payload, headers=headers)

        if response.status_code == 201:
            logging.info("Successfully synced customer")
            return jsonify({"status": "synced"}), 200
        else:
            logging.error(f"External API failed: {response.status_code}")
            return jsonify({"error": "External API failure"}), 502

    except Exception as e:
        logging.error(f"Request error: {str(e)}")
        return jsonify({"error": "Integration error"}), 500


if __name__ == "__main__":
    app.run(port=6000, debug=True)
