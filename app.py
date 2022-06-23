from flask import Flask
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

def add(x,y):
    return x + y

@app.route('/')
def home():
    result = add(2, 3)

    return f"SUM:{result} timenow: {now}"

if __name__ == '__main__':
    # app.run(port=8082)
    result = add(2, 3)
    print(f"SUM:{result} timenow: {now}")

