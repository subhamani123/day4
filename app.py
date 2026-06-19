from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to My Flask Cloud Application</h1>
    <p>Successfully Deployed Using CI/CD Pipeline</p>
    <p>hello world</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
