from flask import Flask
from datetime import datetime

app = Flask(__name__)

def add(x,y):
    return x + y

@app.route('/')
def home():
    result = add(2, 3)
    now = datetime.now()
    return f"SUM:{result} timenow: {now}"

if __name__ == '__main__':
    app.run()
