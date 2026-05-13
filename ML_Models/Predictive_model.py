import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

print("🚀 Starting Predictive Analytics Module...")

# ==========================================
# 1. LOAD HISTORICAL DATA (For Training)
# ==========================================
print("Loading Historical Data...")
# use raw string literals to avoid escape sequence warnings

# read historical files and normalize column names to lowercase for consistency
hist_fact_path = r'C:\Desktop\Data Stuffs\Final Year Project\Datasets\Fact_Performance.csv'
hist_student_path = r'C:\Desktop\Data Stuffs\Final Year Project\Datasets\Dim_Student.csv'

df_hist_fact = pd.read_csv(hist_fact_path)
df_hist_student = pd.read_csv(hist_student_path)

# convert all column names to lowercase to match actual csv headers
for df in (df_hist_fact, df_hist_student):
    df.columns = df.columns.str.lower()

# Extract Semester from course_id (e.g., 'CS_101' -> '1')
# column names are lowercase after normalization
if 'course_id' not in df_hist_fact.columns:
    raise KeyError("Expected 'course_id' column in historical facts")
df_hist_fact['semester'] = df_hist_fact['course_id'].str.split('_').str[1].str[0].astype(int)

# Calculate GPA per semester for historical students
hist_gpa = df_hist_fact.groupby(['student_id', 'semester'])['grade_point'].mean().unstack()
hist_gpa.columns = [f'Sem_{col}_GPA' for col in hist_gpa.columns]
hist_gpa = hist_gpa.reset_index()

# Calculate Final CGPA (Average of all semesters)
hist_gpa['Final_CGPA'] = hist_gpa[[col for col in hist_gpa.columns if 'Sem_' in col]].mean(axis=1)

# Merge with Student Demographics (High School GPA)
# merge using normalized lowercase column names
required_cols = ['student_id', 'high_school_gpa', 'commute_distance_km']
df_train = pd.merge(hist_gpa, df_hist_student[required_cols], on='student_id', how='inner')

# after merging, hist_gpa still has uppercase semester columns – lower everything
# make all column names lowercase for consistent downstream usage
df_train.columns = df_train.columns.str.lower()

# Drop missing values (e.g., students who dropped out early)
df_train = df_train.dropna(subset=['sem_1_gpa', 'sem_2_gpa', 'final_cgpa', 'high_school_gpa'])

# ==========================================
# 2. TRAIN THE MACHINE LEARNING MODEL
# ==========================================
print("Training Linear Regression Model...")

# Define Features (X) and Target (y)
# We predict Final CGPA using only early indicators: Sem 1, Sem 2, and High School GPA
X = df_train[['sem_1_gpa', 'sem_2_gpa', 'high_school_gpa']]
y = df_train['final_cgpa']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
print(f"✅ Model Trained! R2 Score: {r2:.2f} (1.0 is perfect)")
print(f"   Model Weights - Sem 1: {model.coef_[0]:.2f}, Sem 2: {model.coef_[1]:.2f}, HS GPA: {model.coef_[2]:.2f}")

# ==========================================
# 3. LOAD ACTIVE DATA (For Prediction)
# ==========================================
print("\nLoading Active Student Data for Prediction...")
# load active datasets with raw string paths and normalize
active_fact_path = r'C:\Desktop\Data Stuffs\Final Year Project\Datasets\Fact_Active.csv'
active_student_path = r'C:\Desktop\Data Stuffs\Final Year Project\Datasets\Dim_Student_Active.csv'

df_active_fact = pd.read_csv(active_fact_path)
df_active_student = pd.read_csv(active_student_path)

for df in (df_active_fact, df_active_student):
    df.columns = df.columns.str.lower()

# Extract semester from course_id for active data
if 'course_id' not in df_active_fact.columns:
    raise KeyError("Expected 'course_id' column in active facts")
df_active_fact['semester'] = df_active_fact['course_id'].str.split('_').str[1].str[0].astype(int)

# Calculate GPA per semester for active students
# df_active_fact columns are lowercase
active_gpa = df_active_fact.groupby(['student_id', 'semester'])['grade_point'].mean().unstack()
active_gpa.columns = [f'Sem_{col}_GPA' for col in active_gpa.columns]
active_gpa = active_gpa.reset_index()
# make columns lowercase as well
active_gpa.columns = active_gpa.columns.str.lower()

# Merge with Active Student Demographics
df_predict = pd.merge(active_gpa, df_active_student[['student_id', 'high_school_gpa']], on='student_id', how='inner')

# Filter for students who have completed Sem 1 and Sem 2
# use lowercase column names
df_predict = df_predict.dropna(subset=['sem_1_gpa', 'sem_2_gpa', 'high_school_gpa'])

# ==========================================
# 4. RUN PREDICTIONS
# ==========================================
print("Running Predictions on Active Students...")
# feature columns are lowercase after merge
X_active = df_predict[['sem_1_gpa', 'sem_2_gpa', 'high_school_gpa']]

# Predict Final CGPA
# store result in lowercase column name to stay consistent
df_predict['predicted_final_cgpa'] = model.predict(X_active)

# Cap predictions at 10.0 (Max CGPA)
df_predict['predicted_final_cgpa'] = df_predict['predicted_final_cgpa'].clip(upper=10.0).round(2)

# Select final columns for Power BI
final_predictions = df_predict[['student_id', 'predicted_final_cgpa']]

# Export to CSV
final_predictions.to_csv('Predicted_CGPA.csv', index=False)
print("✅ SUCCESS: Predictions saved to 'Predicted_CGPA.csv'. Ready for Power BI!")