# 🏥 Health Insurance Premium Predictor

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

Welcome to the **Health Insurance Premium Predictor**! This project utilizes Machine Learning to estimate health insurance premiums based on various personal, health, and socio-economic factors.

## 🌟 Key Features

*   **Interactive UI**: A fully redesigned, user-friendly interface built with Streamlit.
*   **Structured Inputs**: Easy-to-use forms organized into Personal Information, Health Profile, and Socio-Economic Details.
*   **Real-time Predictions**: Instant estimation of your health insurance costs using a pre-trained ML model.
*   **Modern Aesthetics**: Clean design with custom CSS, visual separators, and clear result cards.

## 🛠️ Technology Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Model Deployment:** `prediction_helper.py` serving a pre-trained model

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Make sure you have Python installed. You can install the required dependencies using pip.

```bash
git clone https://github.com/your-username/ml-project-premium-prediction.git
cd ml-project-premium-prediction
pip install -r requirements.txt
```

### Running the App

To start the Streamlit application locally, run the following command in your terminal:

```bash
streamlit run main.py
```
This will start a local server, and you can view the application in your browser (typically at `http://localhost:8501`).

## 📁 Project Structure

```text
├── artifacts/              # Contains the pre-trained ML models and scalers
├── main.py                 # Main Streamlit application containing UI and layout
├── prediction_helper.py    # Script handling input preprocessing and prediction
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🤖 How it Works

The application collects user inputs such as age, BMI, medical history, and insurance plan tier. It preprocesses these inputs, normalizes health risk scores, scales the numerical values, and then feeds them into trained Machine Learning models to output an estimated premium cost.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to check [issues page](https://github.com/your-username/ml-project-premium-prediction/issues).

## 📝 License

This project is [MIT](https://choosealicense.com/licenses/mit/) licensed.
