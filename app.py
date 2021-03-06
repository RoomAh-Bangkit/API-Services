from flask import Flask, jsonify, make_response, request, render_template
from inference import get_category, plot_category
from datetime import datetime

app = Flask(__name__)

@app.route('/loadimg', methods=['GET', 'POST'])
def roomah():
    if request.method == 'POST':
    # POST method to post the results file
        # Read file from upload
        img = request.files['file']
        # Get category of prediction
        image_category = get_category(img)
        # Plot the category
        return make_response(jsonify({"error":"false","message":"success","result":image_category[0]}))
    return make_response(jsonify({"error":"true","message":"failed"}))

if __name__ == '__main__':
    app.run(debug=True)
