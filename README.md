# ASIAN PAINTS STOCK PRICE PREDICTION 📈

This **machine learning-based web application** predicts the **High, Low, and Closing prices** of Asian Paints stock based on the **previous closing price**. It is built using **Streamlit** and utilizes trained regression models.

---

## 📊 About the Data
The dataset used for this project was sourced from **[Kaggle](https://www.kaggle.com/)** and contains historical stock price data of **Asian Paints Ltd.** from year **2000 to 2021** It includes the following features:
- Date
- Open
- High
- Low
- Close
- Volume
- Prev Close (engineered feature)

---

## 💻 How It Works
1. Users input the **previous closing price** of the stock.
2. The application uses trained regression models to predict:
   - **High Price**
   - **Low Price**
   - **Closing Price**
3. The predictions are displayed with visualizations:
   - A **line plot** for stock prices.
   - A **bar chart** for comparison.

---

## 🧪 Machine Learning Models Used
The following models were trained and tested for performance:

| Model                     | R² Score | MSE         | MAE       | RMSE      |
|---------------------------|----------|-------------|-----------|-----------|
| Linear Regression         | 0.9801   | 20616.3216  | 17.6968   | 143.5838  |
| Lasso                     | 0.9801   | 20616.1321  | 17.6964   | 143.5832  |
| Ridge                     | 0.9801   | 20613.8700  | 17.6909   | 143.5753  |
| ElasticNet                | 0.9801   | 20616.1320  | 17.6964   | 143.5832  |
| DecisionTreeRegressor     | 0.9802   | 20502.9616  | 21.0955   | 143.1886  |
| RandomForestRegressor     | 0.9804   | 20317.4747  | 20.1077   | 142.5394  |
| GradientBoostingRegressor | 0.9805   | 20172.3202  | 18.7246   | 142.0293  |
| AdaBoostRegressor         | 0.9792   | 21511.1363  | 48.4669   | 146.6668  |

---

## 🔧 Best Model
The **GradientBoostingRegressor** achieved the best performance with:
- **R² Score**: 0.9805
- **MSE**: 20172.3202
- **MAE**: 18.7246
- **RMSE**: 142.0293

Best Parameters:  
`{'learning_rate': 0.05, 'max_depth': 3, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 200}`

---

## 🛠️ Tech Stack
The following libraries and technologies were used:
- **Streamlit**: For creating the web application.
- **Pandas**: For data manipulation.
- **Scikit-learn**: For machine learning.
- **Seaborn & Matplotlib**: For visualizations.
- **NumPy**: For numerical computations.

---

