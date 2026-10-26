# loader.py
import pandas as pd

# Load the datasets
intake_data = pd.read_csv("Austin_Animal_Center_Intakes-10-23-26.csv")
outcome_data = pd.read_csv("Austin_Animal_Center_Outcomes-10-23-26.csv")