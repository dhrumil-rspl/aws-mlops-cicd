from flask import Flask, send_from_directory
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv('datasets/dataset.csv')
    return df.to_html()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
