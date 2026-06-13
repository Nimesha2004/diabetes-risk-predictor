import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# CSV File load
try:
    data=pd.read_csv('diabetes_data.csv')
    print("Data Loaded Successfully!\n")
except FileNotFoundError:
    print("Error :'diabetes_data.csv'file not found. please check the path .")
    exit()
    
    
# Seperate Features (X) and Target (Y)  
X=data[['Glucose','BMI','Age']]
Y=data['Outcome']

# Devide Data (Train 80%,Test 20% )
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
      
# Train Logistic Regression model
model = LogisticRegression() 
model.fit(X_train,Y_train)

# Check Accuracy in Model
Y_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test,Y_pred)
print(f"Model Traning Complete.Accuracy : {accuracy*100:.2f}%\n")

# Predict User input Data 
print("----------------DIABEDES RISK PREDICTION SYSTEM-----------------")
try:
    glucose=float(input("Enter Glucose Level (mg/dl) : "))
    bmi=float(input("Enter BMI (e.g,23.5): "))
    age=int(input("Enter Age :"))
    
    # Prediction
    prediction=model.predict([[glucose,bmi,age]])
    
    print("\n-----Result-----")
    if prediction[0]==1:
        print("⚠️ Warning : High Risk of Diabetes. Please consult a doctor.")
    else:
        print("✅ Safe : Low risk of Diabetes. Keep maintaining helthy lifestyle.")
except ValueError:
    print("Please enter valid numeric valuse.")
        
