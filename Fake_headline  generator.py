from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Load word lists once at startup
with open("list.txt", "r") as f:
    words = [line.strip() for line in f if line.strip()]

with open("vocab.txt", "r") as f:
    vocab_words = [line.strip() for line in f if line.strip()]

with open("places_and_things.txt", "r") as f:
    places_and_things = [line.strip() for line in f if line.strip()]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate')
def generate():
    headline = (
        f"BREAKING NEWS: {random.choice(words).upper()} "
        f"{random.choice(vocab_words).upper()} "
        f"{random.choice(places_and_things).upper()}"
    )
    return jsonify({"headline": headline})


if __name__ == '__main__':
    app.run(debug=True, port=5001)

