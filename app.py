#Importing libraries
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

#Importing Models
high_model=pickle.load(open('high_pred_model.pkl','rb'))
close_model=pickle.load(open('regression_model.pkl','rb'))
low_model=pickle.load(open('low_pred_model.pkl','rb'))


#Giving title and markdowns
st.title("ASIAN PAINTS STOCK PRICE PREDICTION")
st.markdown("""


This is a **machine learning-based web application** built using **Streamlit** that predicts the **High, Low, and Closing prices** of Asian Paints stock based on the **previous closing price**.

## 📊 About the Data

The dataset used in this project was sourced from **[Kaggle](https://www.kaggle.com/)** and contains historical stock price data of **Asian Paints Ltd.** It includes features such as:
- Date
- Open
- High
- Low
- Close
- Volume
- Prev Close (engineered feature)

""")

#taking input
close_price_input=st.text_input("Enter Previous closing price of Stock")

#Button action
if st.button("PREDICT") :
    try:
         
         cp=float(close_price_input)

         #Conversion of input to dataFrame
         close_price=pd.DataFrame([[cp]],columns=['Prev Close'])

         #Making Predictions
         high = float(high_model.predict(close_price)[0])
         low = float(low_model.predict(close_price)[0])
         close = float(close_model.predict(close_price)[0])

         #Showing results
         st.success("Predicted Values:")
         st.markdown(f"<h2 style='color: green;'>Predicted Highest Price: ₹{high:.2f}</h2>", unsafe_allow_html=True)
         st.markdown(f"<h2 style='color: red;'>Predicted Lowest Price: ₹{low:.2f}</h2>", unsafe_allow_html=True)
         st.markdown(f"<h2 style='color: white;'>Predicted Closing Price: ₹{close:.2f}</h2>", unsafe_allow_html=True)

         pred_df = pd.DataFrame({
            'Price Type': ['High', 'Low', 'Close'],
            'Predicted Price': [high, low, close]
        })

        # Plot
         fig = plt.figure()
         sns.lineplot(data=pred_df, x='Price Type', y='Predicted Price', marker='o')
         plt.title("Predicted Stock Prices")
         plt.xlabel("Price Type")
         plt.ylabel("Price (₹)")
         st.pyplot(fig)
         fig1=plt.figure()
         sns.barplot(data=pred_df,x='Price Type', y='Predicted Price')
         plt.title("Predicted Stock Prices")
         plt.xlabel("Price Type")
         plt.ylabel("Price (₹)")
         st.pyplot(fig1)
    except ValueError :
      st.error("INVALID INPUT PLEASE ENTER A NUMBER......")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
  

 




