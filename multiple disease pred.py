# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 01:31:46 2023

@author: Shradha Koot
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

db_model = pickle.load(open("diabetes_model.sav",'rb'))

hd_model = pickle.load(open("heart_disease_model.sav",'rb'))

pk_model = pickle.load(open("parkinsons_model.sav",'rb'))


# sidebar for navigation:
with st.sidebar:
    selected = option_menu("multiple disease prediction ",
                           
                           ['Diabetes prediction',
                            'Heart disease prediction',
                            'Parkinsons disease prediction'],
                           
                           icons = ['activity', 'heart', 'person'],
                           
                           default_index = 0)

# diabetes prediction page:
if (selected == 'Diabetes prediction'):
    
    # page title
    st.title('Diabetes prediction using ML')
    
   # getting input data :
       
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('number of pregnancies: ')
        
    with col2:
        Glucose = st.text_input('Glucose level: ')
        
    with col3:
        BloodPressure = st.text_input('Blood pressure value: ')
        
    with col1:
        SkinThickness = st.text_input('skin thickness value: ')
        
    with col2:
        Insulin = st.text_input('Insulin level: ')
        
    with col3:
        BMI = st.text_input('Bmi value: ')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes predigree: ')
        
    with col2:
        Age  = st.text_input('Age of person: ')
    
   
    #Pregnancies = st.text_input('number of pregnancies: ')
    #Glucose = st.text_input('Glucose level: ')
    #BloodPressure = st.text_input('Blood pressure value: ')
    #SkinThickness = st.text_input('skin thickness value: ')
    #Insulin = st.text_input('Insulin level: ')
    #BMI = st.text_input('Bmi value: ')
    #DiabetesPedigreeFunction = st.text_input('Diabetes predigree: ')
    #Age  = st.text_input('Age of person: ')
    
    
    # code for prediction
    diab_diagnosis = ''
    
    
    # creating button for prediction:
    if st.button('Diabetes test result'):
        diab_pred = db_model.predict([[Pregnancies,
                                      Glucose,
                                      BloodPressure,
                                      SkinThickness,
                                      Insulin,
                                      BMI,
                                      DiabetesPedigreeFunction,
                                      Age]])
        
        if (diab_pred[0] == 1):
            diab_diagnosis = 'The person is diabetic'
            
        else:
            diab_diagnosis = 'The person is not diabetic'
            
    st.success(diab_diagnosis)
    
    
# heart disease prediction page:
if (selected == 'Heart disease prediction'):
    
    # page title
    st.title('Heart disease prediction using ML')
    
    # getting input data :
        
    col1, col2, col3 = st.columns(3)
     
    with col1:
         age = st.text_input('Age of person: ')
         
    with col2:
        sex = st.text_input('Gender: ')
        
    with col3:
        cp = st.text_input('Chest pain type: ')
        
    with col1:
        trestbps = st.text_input('Resting blood pressure: ')
        
    with col2:
        chol = st.text_input('Serum cholestoral in mg/dl: ')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl: ')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results: ')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved: ')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina: ')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise: ')
    
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment: ')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy: ')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')


    hd_diagnosis = ''
    
    
    # creating button for prediction:
    if st.button('Heart disease test result'):
        hd_pred = db_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if (hd_pred[0] == 1):
            hd_diagnosis = 'The person has heart isease'
            
        else:
            hd_diagnosis = 'The person does not have heart disease'
            
    st.success(hd_diagnosis)
    
    
    

# parkinsons prediction page:
if (selected == 'Parkinsons disease prediction'):
    
    # page title
    st.title('parkinsons prediction using ML')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = pk_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

