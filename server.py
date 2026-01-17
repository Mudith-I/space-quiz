from flask import Flask, send_file, request, jsonify
from collections import Counter

app = Flask(__name__)

HOUSE_DESCRIPTIONS = {
    "Sun": "Radiant leader with confidence.",
    "Mercury": "Fast-thinking communicator.",
    "Venus": "Harmonious and empathetic.",
    "Earth": "Grounded and dependable.",
    "Mars": "Bold and fearless.",
    "Jupiter": "Optimistic explorer.",
    "Saturn": "Disciplined strategist.",
    "Uranus": "Innovative rebel.",
    "Neptune": "Dreamy visionary.",
    "Pluto": "Deep and introspective."
}

@app.route("/")
def home():
    return send_file("index.htm")  # instead of render_template

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    answers = data["answers"]

    counts = Counter(answers)
    house = counts.most_common(1)[0][0]

    return jsonify({
        "house": house,
        "description": HOUSE_DESCRIPTIONS[house]
    })

if __name__ == "__main__":
    app.run()
