import numpy as np
import pandas as pd
import json
from preprocessing.text_preprocessing import clean_text
from preprocessing.csv_preprocessing import Preprocessing
from sklearn.preprocessing import LabelEncoder
from Feature_Extraction.Modified_weighted_TFIDF import Modified_weighted_TFIDF
from Feature_Extraction.Stastical_text_features import stats_feat_text
csv_path = "Datasets/Dataset1/zomato.csv"

opened_csv = pd.read_csv("Datasets/Dataset1/zomato.csv", encoding='ISO-8859-1')

restaurant_data = opened_csv.iloc[:, :16].copy()

user_data_csv = opened_csv.iloc[:, 16:]
restaurant_data["User_data"] = ""
for i in range(user_data_csv.shape[0]):
    user_data_text = (str(user_data_csv["Rating color"].iloc[i]) + " " + str(
        user_data_csv["Rating text"].iloc[i]) + " " + str(user_data_csv["Votes"].iloc[i]))

    restaurant_data.loc[i, "User_data"] = user_data_text

label = np.round(user_data_csv["Aggregate rating"])
le = LabelEncoder()
out = le.fit_transform(label)

only_res_data = restaurant_data.drop(columns=["User_data"])

restaurant_data["clean_text"] = restaurant_data["User_data"].apply(clean_text)

preprocessed_file = Preprocessing(only_res_data)

X_transformed, TFID_object = Modified_weighted_TFIDF(restaurant_data["clean_text"][:2000], out[:2000])

X_transformed = X_transformed.to_numpy()

Stats_feat = stats_feat_text(restaurant_data["clean_text"][:2000])