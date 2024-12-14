from flask import Flask, request, jsonify, render_template
from traffic_analyzer import analyze_packet
from ml_model import detect_anomaly
from email_parser import extract_metadata
from graph_analyzer import build_graph, get_clusters

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/traffic', methods=['POST'])
def analyze_traffic():
    data = request.json  # Example: {"packet_size": 500, "time_interval": 0.2}
    anomaly = detect_anomaly(data)
    return jsonify({"anomaly": anomaly})

@app.route('/email', methods=['POST'])
def email_metadata():
    raw_email = request.data.decode('utf-8')
    metadata = extract_metadata(raw_email)
    return jsonify(metadata)

@app.route('/graph', methods=['POST'])
def analyze_graph():
    edges = request.json.get("edges")
    clusters = get_clusters(edges)
    return jsonify({"clusters": clusters})

if __name__ == '__main__':
    app.run(debug=True)
