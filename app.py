from flask import Flask, request, render_template
import pickle
import numpy as np
from dashboard import add_dashboard  # Import the dashboard integration function

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Attach the dashboard to the Flask app
dash_app = add_dashboard(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    brand = request.form.get('brand')
    ratings = float(request.form['Ratings'])
    ram = float(request.form['RAM'])
    rom = float(request.form['ROM'])
    mobile_size = float(request.form['Mobile_Size'])
    primary_cam = float(request.form['Primary_Cam'])
    selfi_cam = float(request.form['Selfi_Cam'])
    battery_power = float(request.form['Battery_Power'])
    features = np.array([[ratings, ram, rom, mobile_size, primary_cam, selfi_cam, battery_power]])

    # Make prediction
    predicted_price = model.predict(features)

    # Format the output price
    output = '{0:.2f}'.format(predicted_price[0]) 

    return render_template('index.html', pred=f'Predicted Price: {output}',
                           brand=brand, ram=ram, rom=rom, ratings=ratings,
                           mobile_size=mobile_size, primary_cam=primary_cam,
                           selfi_cam=selfi_cam, battery_power=battery_power)

if __name__ == '__main__':
    app.run(debug=True)
