<h1 style="color: #2F4F4F; text-align:center;">
  <b>Earthquake Predictor Project</b>
</h1>

<p style="text-align:center;">
  <em>Predict earthquake magnitude and depth using Machine Learning</em>
</p>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">1. Overview</h2>

<p>
  This repository demonstrates a <strong>machine learning project</strong> for predicting earthquake magnitude and depth based on historical data. 
  The project includes a neural network model, a Flask API for local testing, and a Jupyter Notebook for model training and experimentation.
</p>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">2. Project Structure</h2>

<pre>
Earthquake Predictor/
├── datasets/                    # CSV files (if any)
├── notebook/
│   ├── earthquake_predict.ipynb # Jupyter Notebook for training
│   └── saved_models_scalar/     # Saved model and scaler files
├── templates/
│   └── index.html               # Frontend HTML file
├── app.py                       # Flask backend
├── earthquake_heatmap.html      # Optional visualization output
├── requirements.txt             # Python dependencies
└── venv1/                       # Virtual environment (ignored)
</pre>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">3. Installation</h2>

<ol>
  <li>
    <strong>Clone the repository:</strong>
    <pre><code>git clone https://github.com/deephabiswashi/Earthquake-Predictor.git
cd Earthquake-Predictor</code></pre>
  </li>
  <li>
    <strong>Create and activate a virtual environment:</strong>
    <pre><code>python -m venv venv1
# For macOS/Linux:
source venv1/bin/activate
# For Windows:
venv1\Scripts\activate</code></pre>
  </li>
  <li>
    <strong>Install dependencies:</strong>
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>
</ol>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">4. Local Testing </h2>

<ol>
  <li>
    <strong>Train the Model (Jupyter Notebook):</strong>
    <pre><code>notebook/earthquake_predict.ipynb</code></pre>
    <p>Run all cells to train the model and save the files <code>earthquake_model.keras</code> and <code>scaler.pkl</code>.</p>
  </li>
  <li>
    <strong>Run the Flask App:</strong>
    <pre><code>python app.py</code></pre>
    <p>This starts the Flask server at <code>http://localhost:5000</code>.</p>
  </li>
  <li>
    <strong>Access the Frontend:</strong>
    <p>Open your browser and navigate to <code>http://localhost:5000</code> to use the prediction interface.</p>
  </li>
</ol>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<h2 style="color:#4169E1;">5. License</h2>

<p>
  This project is licensed under the <strong>Apache License 2.0</strong>.
</p>

<hr style="border: 1px solid #ccc; margin: 20px 0;" />

<p style="text-align:center;">
  <em>Made with ❤️ by Deep Habiswashi</em>
</p>
