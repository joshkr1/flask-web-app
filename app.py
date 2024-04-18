# Import Flask and other modules
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, welcome to my Flask web app!'

# Define a route for an about page
@app.route('/about')
def about():
    return 'This is a simple Flask web app.'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

