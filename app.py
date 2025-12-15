from flask import Flask, render_template, request
from PIL import Image
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files.get("image")

        if file:
            image = Image.open(file)
            image = image.resize((224, 224))

            # Simple MVP simulation logic
            detected = random.choice([True, False])

            if detected:
                result = "Kidney Stone Found"
            else:
                result = "No Kidney Stone Found"

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
