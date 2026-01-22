import streamlit as st
import numpy as np
import pickle   

model = pickle.load(open('heart-disease-project\src\model/heart_disease_model.pkl', 'rb'))
scaler = pickle.load(open('heart-disease-project\src\model/scaler.pkl', 'rb'))

st.title('Prediction de la maladie cardiaque')
st.write('Entrez les caractéristiques du patient pour prédire la maladie cardiaque')
age = st.number_input('Âge',20,100)
sex = st.selectbox('Sexe',[0,1],format_func=lambda x:"F" if x==0 else "M" )
cp =st.selectbox('douleur thoracique',[0,1,2,3])
trestbps = st.number_input('Tension artérielle au repos',80,200,120)
chol = st.number_input('Cholestérol sérique (mg/dl)',100,600,200)
fbs =st.selectbox('taux de sucre dans le sang > 120 mg/dl',[0,1])
restcg =st.selectbox('ecg de repos',[0,1,2])
thalach = st.number_input('fréquence cardiaque maximale atteinte',60,250,150)
exang =st.selectbox('angine',[0,1] )
oldpeak = st.number_input('dépression du segment ST induite ',0.0,6.0,1.0)
slope =st.selectbox('la pente du segment ST ',[0,1,2] )
ca =st.selectbox('nombre de vaisseaux majeurs ',[0,1,2,3,4])
thal =st.selectbox('thalassemie ',[0,1,2,3] )
if st.button("Predire"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]])
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    if prediction[0] == 1:
        st.success('Le patient est susceptible d\'avoir une  maladie cardiaque')
    else:
        st.success('Le patient n\'a pas la maladie cardiaque')
