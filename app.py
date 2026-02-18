from flask import Flask, request, jsonify
import requests
import logging
from config import EXTERNAL_API_URL, API_KEY

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    filename="integration.log",
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/sync-customer", methods=["POST"])
def sync_customer():
    data = request.json

    if not data or "customer_id" not in data:
        logging.warning("Invalid payload received")
        return jsonify({"error": "Invalid payload"}), 400

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
        response = requests.post(
            EXTERNAL_API_URL,
            json=transformed_payload,
            headers=headers,
            timeout=5
        )

        if response.status_code == 201:
            logging.info(f"Customer {data['customer_id']} synced successfully")
            return jsonify({"status": "synced"}), 200
        else:
            logging.error(f"External API failed: {response.status_code}")
            return jsonify({"error": "External API failure"}), 502

    except requests.exceptions.RequestException as e:
        logging.error(f"Integration error: {str(e)}")
        return jsonify({"error": "Integration error"}), 500


if __name__ == "__main__":
    app.run(port=6000, debug=True)
