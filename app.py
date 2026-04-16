# Create a simple Flask web application.
# Requirements:
# 1. Import Flask and create an app instance.
# 2. Create a route '/' that returns the string:
#    "Multi-Cloud Failover System Running 🚀"
# 3. Create another route '/status' that returns JSON with:
#    AWS: "UP"
#    GCP: "UP"
#    Active: "AWS"
# 4. Run the app in debug mode on localhost (port 5000).

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Multi-Cloud Failover System Running 🚀"

@app.route('/status')
def status():
    return jsonify({
        "AWS": "UP",
        "GCP": "UP",
        "Active": "AWS"
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)