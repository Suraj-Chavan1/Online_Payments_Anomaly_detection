


import pickle
import streamlit as st
from streamlit_option_menu import option_menu
# Load the model

model = pickle.load(open('D:\ML\deploymodel\Model1.sav', 'rb'))

model = pickle.load(open('D:\ML\deploymodel\credit_card.sav', 'rb'))

model2 = pickle.load(open("D:\ML\deploymodel\Credit_Score_Classification.sav", 'rb')) 
    
with st.sidebar:
    
    selected = option_menu('Barclays',
                          
                          ["Home","Stock Anamoly Aetection","Banking Anamoly detection",
                           'Credit-card',
                           'Credit Score Classification',"Thank You"],
                          icons=["","","",""],
                          default_index=0)


if selected=="Home":
    st.title('Welcome to Barclays')
    st.image('https://www.pymnts.com/wp-content/uploads/2022/07/barclays-copper-stake.jpg')
    st.write('Select the model from the sidebar to make predictions')
    st.write("1 model is for stock anamoly detection")
    st.write("2nd model is for banking anamoly detection")
    st.write("3rd model is for credit card anamoly detection")

if selected == 'Stock Anamoly Aetection':
    st.title('Stock Anamoly Aetection')
    st.markdown(
        "Read More about the dataset [Kaggle](https://finance.yahoo.com/quote/GS/history?period1=1230854400&period2=1576454400&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true&guccounter=1&guce_referrer=aHR0cHM6Ly9jb2xhYi5yZXNlYXJjaC5nb29nbGUuY29tLw&guce_referrer_sig=AQAAALxTgaH-gTiOO7Buk3c9L23kARngePm3YPKDu_PUPqFtitW3B55uBa303QUhUAkJ3tb7eaQ_rEe5H4cQrOm0i7_emZ35cAom4RADhntujr_s8ND37dPdjc0Zy1-blGnx52Mlnp9ptaOU_FhxVD9mSGJKUbcfSCetoac9K0tGxHZE)"
        "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1ZsaAYRDbOIuXcvloagGyxSK9HqVb3mk3?usp=sharing)"
    )
    st.markdown("Not able to provide the input fields for the model as it is a time series data and the model is trained on the same data.")
    
    
if selected == 'Banking Anamoly detection':
    st.title('Online Payments Anomaly detection')
    
    st.markdown(
        "Read More about the dataset [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1/data)"+
        "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1QL_wDSGfVg38KcPzRanDnA6KV-_7OoKa?usp=sharing) "
        
    )
        # Input fields for the four values
    value1 = st.number_input('Type : CASH OUT=1 ,  PAYMENT=2 ,  CASH IN=3 ,  TRANSFER=4 ,  DEBIT=5', value=0, step=1)
    value2 = st.number_input('Amount', value=0, step=1)
    value3 = st.number_input('Old Balance In Account', value=0, step=1)
    value4 = st.number_input('New Balance IN Account', value=0, step=1)
    
    # Button to trigger the prediction
    if st.button('Predict'):
        # Make the prediction
        prediction = model.predict([[value1, value2, value3, value4]])
        # Display the prediction 
        ans = int(prediction[0])
        print(ans)
        if ans == 1:
            st.success('Prediction: Fraud')
        else:
            st.success('Prediction: Not Fraud')
            
            
            
if(selected == 'Credit-card'):
    st.title('Credit-card Anamoly detection')
    st.markdown(
        "Read More about the dataset [Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)"+
        "Read More about the Model Used [Google Collab Link](https://colab.research.google.com/drive/1DFg9jRAKD24wURDvdIJbx2rQLYwhyXD7?usp=sharing) "
        
    )
    # Input fields for the four values
    col1, col2, col3 = st.columns(3)
    
    with col1:
        value1 = st.number_input('Time', value=0, step=1)
        value2 = st.number_input('V1', value=0, step=1)
        value3 = st.number_input('V2', value=0, step=1)
        value4 = st.number_input('V3', value=0, step=1)
        value5 = st.number_input('V4', value=0, step=1)
    
    with col2:
        value6 = st.number_input('V5', value=0, step=1)
        value7 = st.number_input('V6', value=0, step=1)
        value8 = st.number_input('V7', value=0, step=1)
        value9 = st.number_input('V8', value=0, step=1)
        value10 = st.number_input('V9', value=0, step=1)
    
    with col3:
        value11 = st.number_input('V10', value=0, step=1)
        value12 = st.number_input('V11', value=0, step=1)
        value13 = st.number_input('V12', value=0, step=1)
        value14 = st.number_input('V13', value=0, step=1)
        value15 = st.number_input('V14', value=0, step=1)
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        value16 = st.number_input('V15', value=0, step=1)
        value17 = st.number_input('V16', value=0, step=1)
        value18 = st.number_input('V17', value=0, step=1)
        value19 = st.number_input('V18', value=0, step=1)
        value20 = st.number_input('V19', value=0, step=1)
    
    with col5:
        value21 = st.number_input('V20', value=0, step=1)
        value22 = st.number_input('V21', value=0, step=1)
        value23 = st.number_input('V22', value=0, step=1)
        value24 = st.number_input('V23', value=0, step=1)
        value25 = st.number_input('V24', value=0, step=1)
    
    with col6:
        value26 = st.number_input('V25', value=0, step=1)
        value27 = st.number_input('V26', value=0, step=1)
        value28 = st.number_input('V27', value=0, step=1)
        value29 = st.number_input('V28', value=0, step=1)
        Amount = st.number_input('Amount', value=0, step=1)
    
    
    if(st.button('Predict')):
        prediction = model1.predict([[value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, value21, value22, value23, value24, value25, value26, value27, value28, value29, Amount]])
        ans = int(prediction[0])
        print(ans)
        if ans == 1:
            st.success('Prediction: Fraud')
        else:
            st.success('Prediction: Not Fraud')
            
            
# print("Credit Score Prediction : ")
# a = float(input("Annual Income: "))
# b = float(input("Monthly Inhand Salary: "))
# c = float(input("Number of Bank Accounts: "))
# d = float(input("Number of Credit cards: "))
# e = float(input("Interest rate: "))
# f = float(input("Number of Loans: "))
# g = float(input("Average number of days delayed by the person: "))
# h = float(input("Number of delayed payments: "))
# i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
# j = float(input("Outstanding Debt: "))
# k = float(input("Credit History Age: "))
# l = float(input("Monthly Balance: "))
# features = np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
# print("Predicted Credit Score = ", model.predict(features))       
if(selected == 'Credit Score Classification'):
    st.title('Credit Score Prediction')
    
 

    st.markdown(

        "[Google Collab Link](https://colab.research.google.com/drive/1CAM8oGv-tQqIhXjcxgG-Aq0mw9e1m5T_?usp=sharing) "
        + "the same space, enabling image similarity search. txtai can directly utilize these models."
    )
    
    
    col1, col2, col3 = st.columns(3)

    with col1:
        a = st.number_input('Annual Income', value=0, step=1)
        b = st.number_input('Monthly Inhand Salary', value=0, step=1)
        c = st.number_input('Number of Bank Accounts', value=0, step=1)
        k = st.number_input('Credit History Age', value=0, step=1)

    with col2:
        d = st.number_input('Number of Credit cards', value=0, step=1)
        e = st.number_input('Interest rate', value=0, step=1)
        f = st.number_input('Number of Loans', value=0, step=1)
        l = st.number_input('Monthly Balance', value=0, step=1)

    with col3:
        g = st.number_input('Average number of days delayed by the person', value=0, step=1)
        h = st.number_input('Number of delayed payments', value=0, step=1)
        i = st.number_input('Credit Mix (Bad: 0, Standard: 1, Good: 3)', value=0, step=1)
        j = st.number_input('Outstanding Debt', value=0, step=1)
        
       
    
    if(st.button('Predict')):
        features = [[a,b,c,d,e,f,g,h,i,j,k,l]]
        prediction = model2.predict(features)
        st.success('Predicted Credit Score = {}'.format(prediction[0]))
        
if selected=="Thank You":
    st.title('Thank You')
    st.write('Hope you had a great experience')
    st.write('Please provide your valuable feedback')
    st.write('This is the only small part of th project which we are thinking to build in future. Please provide us chance to work with you. Thank you.')    
    

    
    













