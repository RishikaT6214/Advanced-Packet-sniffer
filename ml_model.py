import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import xgboost as xgb

#  Load and combine both datasets
df1 = pd.read_csv('../datasets/MachineLearningCVE/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
df2 = pd.read_csv('../datasets/MachineLearningCVE/Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv')
df3 = pd.read_csv('../datasets/MachineLearningCVE/Friday-WorkingHours-Morning.pcap_ISCX.csv')
df4 = pd.read_csv('../datasets/MachineLearningCVE/Monday-WorkingHours.pcap_ISCX.csv')
df5 = pd.read_csv('../datasets/MachineLearningCVE/Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv')
df6 = pd.read_csv('../datasets/MachineLearningCVE/Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv')
df7 = pd.read_csv('../datasets/MachineLearningCVE/Tuesday-WorkingHours.pcap_ISCX.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7], ignore_index=True)

#  Clean column names
df.columns = df.columns.str.strip()

#  Drop identifier / non-numeric columns
columns_to_drop = ['Flow ID', 'Source IP', 'Destination IP', 'Timestamp', 'Source Port', 'Destination Port', 'Protocol']
df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

#  Remove missing and infinite values
df = df.replace([float('inf'), -float('inf')], pd.NA).dropna()

#  Encode labels
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])
print("✅ Encoded labels:", label_encoder.classes_)

#  Split features and labels
X = df.drop(['Label'], axis=1)
y = df['Label']

#  Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#  Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

#  Train Random Forest
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)
rf_preds = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_preds)
print(f"🌲 Random Forest Accuracy: {rf_acc:.4f}")

# ⚡ Train XGBoost
xgb_model = xgb.XGBClassifier(eval_metric='mlogloss')
xgb_model.fit(X_train, y_train)
xgb_preds = xgb_model.predict(X_test)
xgb_acc = accuracy_score(y_test, xgb_preds)
print(f"⚡ XGBoost Accuracy: {xgb_acc:.4f}")

#  Save the best model
if xgb_acc > rf_acc:
    joblib.dump(xgb_model, 'traffic_classifier.pkl')
    print("📦 Saved XGBoost as the final model.")
else:
    joblib.dump(rf_model, 'traffic_classifier.pkl')
    print("📦 Saved RandomForest as the final model.")

#  Save scaler and label encoder
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoder, 'label_encoder.pkl')
print("💾 Scaler and label encoder saved.")
