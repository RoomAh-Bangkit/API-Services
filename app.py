from flask import Flask, jsonify, make_response, request, render_template
from inference import get_category, plot_category
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def roomah():
    if request.method == 'POST':
    # POST method to post the results file
        # Read file from upload
        img = request.files['file']
        # Get category of prediction
        image_category = get_category(img)
        # Plot the category
        return make_response(jsonify(image_category))

if __name__ == '__main__':
    app.run(debug=True)