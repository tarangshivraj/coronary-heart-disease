import streamlit as st
import pickle 
# from sklearn.metrics import accuracy_score
# import pandas as pd

st.title('Coronary Heart Disease Predictor')
st.subheader('Official AI ML Project Submission by Tarang Shivraj Jaiswal')

x_test = []
with st.form(key='my_form'):
	age = st.number_input('Age')
	sex = st.selectbox('Sex', ['Female', 'Male', 'Others'])
	cp = st.selectbox('Chest Pain Type', ['0', '1', '2'])
	trestbps = st.number_input('Resting Blood Pressure')
	chol = st.number_input('serum cholestoral in mg/dl')
	fbs = st.selectbox('fasting blood sugar > 120 mg/dl', ['Yes', 'No'])
	restecg = st.selectbox('resting electrocardiographic results', ['0', '1', '2'])
	thalach = st.number_input('maximum heart rate achieved')
	exang = st.selectbox('exercise induced angina', ['0', '1'])
	oldpeak = st.number_input('oldpeak = ST depression induced by exercise relative to rest')
	slope = st.number_input('the slope of the peak exercise ST segment')
	ca = st.selectbox('number of major vessels (0-3) colored by flourosopy', ['0', '1', '2', '3', '4'])
	thal = st.selectbox('Thal', ['Normal', 'Fixed Defect', 'Reversable Defect'])
	submitted = st.form_submit_button('Submit')
if submitted:
	age = int(age)
	if sex == 'Male':
		sex = 1
	else:
		sex = 0
	cp = int(cp)
	print("The chest pain type is of {}".format(cp))
	trestbps = int(trestbps)
	chol = int(chol)
	if fbs == 'Yes': # Can be compared with 'No'
		fbs = 1
	else:
		fbs = 0
	restecg = int(restecg)
	thalach = int(thalach)
	exang = int(exang)
	oldpeak = int(oldpeak)
	slope = int(slope)
	ca = int(ca)
	if thal == 'Normal':
		thal = 0
	elif thal == 'Fixed Defect':
		thal = 1
	else:
		thal = 2  
	x_test = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
# st.success('Streamlit app is running!!')

# df = pd.read_csv('coronary-artery-disease-final.csv')
# target = df['target']

def predict_using_pickle(x_test: list):
	filename = 'coronary-artery-model.sav'
	model = pickle.load(open(filename, 'rb'))
	predictions = model.predict([x_test])
	if predictions == 0:
		st.warning("There is a risk of you having coronary heart disease in the future!")
	else:
		st.balloons()
		st.success("You are not under the risk of coronary heart disease")
	# accuracy = accuracy_score()

if __name__ == '__main__':
	predict_using_pickle(x_test)