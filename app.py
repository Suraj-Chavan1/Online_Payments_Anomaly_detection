


import streamlit as st
import pickle

# Load the model
with open('D:\ML\deploymodel\Model1.sav', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
def main():
    st.title('Online Payments Anomaly detection')
    
    # Input fields for the four values
    value1 = st.number_input('Type', value=0, step=1)
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
            st.success('Prediction: Front')
        else:
            st.success('Prediction: Not Front')

if __name__ == '__main__':
    main()
