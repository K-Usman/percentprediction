import joblib
import streamlit as st 
import numpy as np

model=joblib.load('Percent.sav')

def main():
  st.title("Student Scores Prediction")
  SL=st.text_input('Enter Study Hours:')
  dat=np.array([SL,1])
  dat.reshape(-1,1)
  if st.button("Predict"):
     try: 
        test_prediction=model.predict(dat.reshape(-1,1))
        st.success("Your percentage will be: {}".format(test_prediction[0]))
     except:
        st.error("Please enter Data")
main()