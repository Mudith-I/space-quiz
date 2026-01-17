from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# House descriptions
house_descriptions = {
    "Sun": "Confident and bold leader.",
    "Mercury": "Quick thinker and communicator.",
    "Venus": "Empathetic and harmonious.",
    "Earth": "Reliable and practical.",
    "Mars": "Courageous and adventurous.",
    "Jupiter": "Optimistic and curious.",
    "Saturn": "Disciplined and strategic.",
    "Uranus": "Innovative and rebellious.",
    "Neptune": "Imaginative and reflective.",
    "Pluto": "Wise and introspective."
}

# Serve the HTML
@app.route("/")
def home():
    return send_from_directory(os.getcwd(), "index.htm")

# Serve the MP3
@app.route("/space-music.mp3")
def music():
    return send_from_directory(os.getcwd(), "space-music.mp3")

# Calculate house
@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    answers = data.get("answers", [])

    counts = {}
    for planet in answers:
        counts[planet] = counts.get(planet, 0) + 1

    if counts:
        house = max(counts, key=counts.get)
    else:
        house = "Sun"

    description = house_descriptions.get(house, "")
    return jsonify({"house": house, "description": description})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the port from Render
    app.run(host="0.0.0.0", port=port)        # Listen on all network interfaces