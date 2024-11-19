
## 1. Introduction

### Purpose of the Project
This project aims to develop a system that predicts smartphone prices based on their technical specifications, providing a valuable tool for retailers and consumers. The solution uses machine learning to forecast prices, along with a user-friendly web interface and dashboard for analysis.

### Importance of Price Prediction
With the growing smartphone market, accurate price prediction helps retailers set competitive pricing strategies and enables consumers to evaluate options based on specifications, ensuring value for money.

### Project Scope
The project involves:
- **Price Prediction**: Using a Random Forest regression model to predict smartphone prices.
- **Flask Web Application**: Allowing users to input specifications and view predictions.
- **Dash Dashboard**: Visualizing feature relationships and trends in smartphone data.

---

## 2. Problem Statement

This project addresses the following challenges:
- **Complex Pricing Decisions**: Provides retailers with tools to estimate prices based on key specifications.
- **Data Insights**: Helps analyze how different features (e.g., RAM, battery capacity) influence pricing.
- **Real-Time Predictions**: Offers an interface for instant feedback on price estimates.

---

## 3. Architecture

The architecture of the project includes:
1. **Frontend (Flask Web App)**:
   - Collects user inputs for smartphone specifications.
   - Displays the predicted price based on the machine learning model.
2. **Backend (Flask API)**:
   - Processes data inputs and interacts with the Random Forest model for predictions.
3. **Machine Learning Model**:
   - Trained on a dataset of 836 smartphones with key attributes like RAM, ROM, and camera specifications.
   - Achieves an R² score of 0.91, ensuring accurate predictions.
4. **Dashboard (Dash)**:
   - Displays visualizations for feature analysis, such as price vs RAM or brand vs price.

---

## 4. Dataset

The dataset consists of 836 smartphone models with the following attributes:
- **Brand**: Manufacturer of the smartphone.
- **RAM/ROM**: Memory and storage capacity.
- **Camera Specifications**: Resolution of front and rear cameras.
- **Battery Power**: Battery capacity in mAh.
- **Price**: Target variable for prediction.

---

## 5. Technologies Used

- **Programming Language**: Python
- **Libraries**: Scikit-learn, Flask, Dash, Pandas, NumPy
- **Machine Learning Model**: Random Forest Regressor
- **Frontend**: HTML, CSS, Flask Templates
- **Visualization**: Dash and Plotly

---

## 6. Features

- **Price Prediction**: Enter smartphone specifications and get price estimates.
- **Interactive Dashboard**: Compare features and their impact on pricing.
- **High Accuracy**: Achieves R² = 0.91 and low MSE, ensuring reliable predictions.
- **Scalable Design**: Can accommodate more features or datasets in the future.

---

## 7. Results

![Prediction Image](./path/to/prediction.png)
- **Prediction Accuracy**: 
  - R² score: 0.91
  - Mean Squared Error (MSE): 7309.82
  - Mean Absolute Error (MAE): 2375.18
- **Dashboard**: Provides dynamic visualizations for feature analysis.
- **User Interface**: Allows easy input of specifications and viewing results in real time.

---

## 8. How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aditiaherr/Smartphone-Price-Prediction.git
   cd Smartphone-Price-Prediction
