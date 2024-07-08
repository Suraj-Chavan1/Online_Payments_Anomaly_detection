# Online Payments Anomaly Detection

This repository contains the implementation of an anomaly detection system for online payments. The project aims to identify fraudulent transactions and unusual patterns in payment data using machine learning techniques.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

With the increasing volume of online transactions, detecting fraudulent activities is crucial to ensure the security of payment systems. This project leverages machine learning to build a robust anomaly detection system for identifying suspicious transactions.

## Features

- Data preprocessing and feature engineering
- Anomaly detection using various machine learning models
- Visualization of anomalies and transaction data
- Evaluation metrics for model performance

## Project Structure

Online_Payments_Anomaly_Detection/
├── data/
│ ├── raw/
│ ├── processed/
├── notebooks/
│ ├── EDA.ipynb
│ ├── Model_Training.ipynb
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── model_training.py
│ ├── anomaly_detection.py
├── tests/
│ ├── test_data_preprocessing.py
│ ├── test_feature_engineering.py
│ ├── test_model_training.py
├── README.md
├── requirements.txt
├── setup.py


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Suraj-Chavan1/Online_Payments_Anomaly_detection.git
    cd Online_Payments_Anomaly_detection
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Data Preprocessing:**

    Run the data preprocessing script to clean and prepare the raw data.

    ```bash
    python src/data_preprocessing.py
    ```

2. **Feature Engineering:**

    Generate features from the processed data.

    ```bash
    python src/feature_engineering.py
    ```

3. **Model Training:**

    Train the anomaly detection model using the prepared dataset.

    ```bash
    python src/model_training.py
    ```

4. **Anomaly Detection:**

    Detect anomalies in new transaction data.

    ```bash
    python src/anomaly_detection.py
    ```

## Dataset

The dataset used for this project includes various features related to online transactions. The raw data should be placed in the `data/raw/` directory. Preprocessed and engineered data will be stored in the `data/processed/` directory.

## Model Training

The model training script trains various machine learning models for anomaly detection, including Isolation Forest, One-Class SVM, and Autoencoders. The script evaluates the models using appropriate metrics and selects the best-performing model.

## Results

The results of the anomaly detection, including visualizations and performance metrics, will be saved in the `results/` directory. Detailed analysis and plots can be found in the Jupyter notebooks under the `notebooks/` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
