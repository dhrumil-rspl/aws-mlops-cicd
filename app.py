from flask import Flask, send_from_directory, render_template_string
import pandas as pd
import joblib
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Load dataset
    dataset_path = os.path.join('datasets', 'dataset.csv')
    df = pd.read_csv(dataset_path)

    # Load model
    model_path = 'model.pkl'
    model = joblib.load(model_path)
    
    # Display dataset and model info
    html = f"""
    <h1>Dataset</h1>
    {df.to_html()}
    <h1>Model Information</h1>
    <p>Model: RandomForestClassifier</p>
    <p>Number of features: {model.n_features_in_}</p>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
