from flask import Flask, render_template, request
from scam_detector import check_scam
import os
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        # Case 1: Link check
        url = request.form.get("url")
        if url:
            result = check_scam(url)
            result["link"] = url

        # Case 2: Image upload check
        if "image" in request.files:
            file = request.files["image"]
            if file.filename!= "":
                # Image ka naam se check karenge
                result = check_scam(file.filename)
                result["link"] = f"Uploaded Image: {file.filename}"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)