from flask import Flask, render_template

app = Flask(__name__)

#Home page Route
@app.route('/')
def index():
    #Renders the home page
    return render_template('index.html')

if __name__ == "__main__":
    #Runs the application
    app.run(debug=True)