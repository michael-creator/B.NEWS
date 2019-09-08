from flask import Flask

# Initializing application
app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to B.news'

if __name__=="__main__":
    app.run(debug=True)