import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


def Preprocessing(csv_file):
    le = LabelEncoder()
    categorical_columns = csv_file.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        csv_file[col] = le.fit_transform(csv_file[col])
    numeric_columns = csv_file.select_dtypes(include=['number']).columns
    csv_file[numeric_columns] = csv_file[numeric_columns].fillna(csv_file[numeric_columns].mean())
    std = StandardScaler()

    normalized = std.fit_transform(csv_file)

    return normalized




