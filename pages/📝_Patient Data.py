import numpy as np
import streamlit as st

def churn_pred(pred_input):

    feature_columns = ['credit_score', 'country', 'gender', 'age', 'tenure', 'balance','products_number', 'credit_card','active_member', 'estimated_salary']
    
    df_input = pd.DataFrame([pred_input], feature_columns)  
    
    scale_input = pickled_scaler.transform(df_input)
    
    df_scale = pd.DataFrame(scale_input, feature_columns) 
     
    prediction = pickled_model.predict(df_scale)
    
    return prediction
    

def main():

    
    st.subheader("Enter the details of the patients")
    
    col1, col2 = st.columns(2)
    
    col3,col4 = st.columns(2)
    
    col5,col6 = st.columns(2)
    
    with col1:
        age = st.number_input('Enter the Age',0,100,0,1,'%d')
    
    with col2:
        bmi = st.number_input('Enter the BMI',0,100,0,1,'%f')
        
    with col1:
        glucose = st.number_input('Enter the Glucose Level',0,200,0,1,'%d')
        
    with col2:
        bp = st.number_input('Enter the Blood Pressure (BP)',0,150,0,1,'%d')
        
    with col3:
        insulin = st.number_input('Enter the Insulin level',0,1000,0,1,'%d')
        
    with col4:
        pregnencies = st.number_input('No.of Childrens for the paitents',0,10,0,1,'%d')
        
    
    
    button = st.button("Predict")
      
        

        
if __name__ == '__main__':
    main()
  
  
