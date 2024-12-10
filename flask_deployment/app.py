from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return 'Hello, World!'

# Define another route
@app.route('/about')
def about():
    return 'This is the About page!'

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
