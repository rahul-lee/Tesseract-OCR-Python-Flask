import cv2
import pytesseract
from flask import Flask, render_template
from flask import *

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("upload.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        img = cv2.imread(f.filename)
        config = ('-l eng+due --oem 1 --psm 3')
        extracted_text = pytesseract.image_to_string(img,
                                                     config=config)
        splits = extracted_text.splitlines()
        s = "\n".join(splits)

        return render_template("success.html",
                               name=f.filename,
                               lines=s)


if __name__ == '__main__':
    app.run(debug=True)
