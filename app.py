from flask import Flask, render_template # for load css

app = Flask(__name__)

# Home route that renders your HTML file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Running on port 8000, same as your original script