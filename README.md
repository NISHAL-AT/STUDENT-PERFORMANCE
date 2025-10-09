## Math Score Predictor
A Streamlit web application that predicts a student's math score based on input features. The app leverages a trained machine learning regression model and supports categorical input encoding with label encoders.


#### Live App Link : https://student-mark-predictor.streamlit.app/
### Project Structure
```
student-score-predictor/
│
├── app.py
├── StudentsPerformance.csv
├── linear_model.pkl
├── encoders.pkl
├── stper.ipynb
├── requirements.txt
└── README.md  
```

### Features
Interactive UI for inputting categorical and numerical student details

Automatic encoding of all categorical features using pre-trained label encoders

Predicts math score using a regression model

User-friendly prediction display with Streamlit

Easily customizable for more features and columns

### Installation

- Clone this repository or download the project files.
- Install Python (3.8+ recommended).

- Install all dependencies:
```
pip install -r requirements.txt
# Ensure linear_model.pkl and encoders.pkl are present in the project directory.
```

- Run the Streamlit application:

```
streamlit run app.py
# In the browser, input student details—both categorical and numerical—using the form.
```
Click the Predict button to see the predicted math score.


### File	Description
```
app.py	                  -->   Streamlit app for prediction
StudentsPerformance.csv   -->	  Original data for EDA/model training
requirements.txt	      -->   Python dependencies
linear_model.pkl	      -->   Trained regression model
encoders.pkl	          -->   Pre-trained label encoders for categorical columns
stper.ipynb	              -->   EDA and machine learning workflow notebook
```

### Requirements
```
Python 3.8+

streamlit

pandas

joblib

scikit-learn

```
### Screenshots

<img width="1555" height="864" alt="image" src="https://github.com/user-attachments/assets/8e77b47f-e150-4118-8e3c-d6ff8e98a435" />


### License
This project is open source and free to use for educational purposes.

Let me know if you want to customize or expand this README for specific deployment instructions or acknowledgements.

### Author : Nishal A T
