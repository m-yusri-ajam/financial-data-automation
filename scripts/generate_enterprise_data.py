import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Create the data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')
    print("📁 Created 'data' directory.")

# Setting a seed for reproducibility
np.random.seed(42)

# 1. GENERATE FINOPS DATA (1000 Rows)
# Simulating a month of AWS/Cloud Infrastructure billing
rows = 1000
dates = [datetime(2026, 3, 1) + timedelta(hours=i) for i in range(rows)]
vendors = ['Amazon AWS', 'Microsoft Azure', 'Google Cloud', 'Cloudflare', 'Datadog']

ledger_data = {
    'Transaction_ID': [f'TXN-{10000 + i}' for i in range(rows)],
    'Date': dates,
    'Vendor': [random.choice(vendors) for _ in range(rows)],
    'Amount_USD': np.round(np.random.uniform(50.0, 5000.0, size=rows), 2),
    'GL_Code': [random.choice([50201, 50202, 50305]) for _ in range(rows)]
}

df_ledger = pd.DataFrame(ledger_data)
df_ledger.to_csv('data/internal_ledger.csv', index=False)

# 2. GENERATE SAP PROJECT DATA (Complex WBS Structure)
# Simulating 50 different Engineering Projects
project_count = 50
sap_data = {
    'WBS_Element': [f'ZA-102-{100 + i}' for i in range(project_count)],
    'Project_Name': [f'Infrastructure_Upgrade_Phase_{i}' for i in range(project_count)],
    'Budget_Released': np.random.randint(500000, 10000000, size=project_count),
}

df_sap = pd.DataFrame(sap_data)
# Create "Actuals" (some over budget, some under)
df_sap['Actual_Costs'] = (df_sap['Budget_Released'] * np.random.uniform(0.4, 1.1, size=project_count)).round(2)
df_sap['Commitments'] = (df_sap['Budget_Released'] * 0.1).round(2)
df_sap.to_csv('data/raw_sap_export.csv', index=False)

# 3. GENERATE INDUSTRIAL TELEMETRY (Continuous Sensor Data)
# 24 hours of data recorded every 5 minutes
sensor_readings = 288 
telemetry_data = {
    'Timestamp': [datetime(2026, 3, 23, 0, 0) + timedelta(minutes=5*i) for i in range(sensor_readings)],
    'Inlet_Flow': np.random.normal(45, 2, size=sensor_readings).round(2),
    'Temperature_C': np.random.normal(180, 5, size=sensor_readings).round(2),
    'Pressure_Bar': np.random.normal(12, 0.5, size=sensor_readings).round(2),
}

df_telemetry = pd.DataFrame(telemetry_data)
# Engineering Logic: Purity is a function of Temperature (Optimization Target)
# We add "Noise" to make it realistic
df_telemetry['Purity_%'] = (91 - abs(df_telemetry['Temperature_C'] - 180) * 0.5 + np.random.normal(0, 0.2, size=sensor_readings)).round(2)
df_telemetry.to_csv('data/process_telemetry.csv', index=False)

print(f"✅ Success! Generated:")
print(f"- {len(df_ledger)} rows for FinOps Reconciliation")
print(f"- {len(df_sap)} projects for SAP Analytics")
print(f"- {len(df_telemetry)} sensor readings for Industrial Optimization")
