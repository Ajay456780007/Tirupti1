import numpy as np
import pandas as pd
import json

csv_path = "Datasets/Dataset1/zomato.csv"

opened_csv = pd.read_csv("Datasets/Dataset1/zomato.csv", encoding='ISO-8859-1')

restaurant_data = opened_csv.iloc[:, :16]

user_data_csv = opened_csv.iloc[:, 16:]

with open("Datasets/Dataset1/file1.json", "r") as file1:
    json1 = json.load(file1)

with open("Datasets/Dataset1/file1.json", "r") as file2:
    json2 = json.load(file2)

with open("Datasets/Dataset1/file1.json", "r") as file3:
    json3 = json.load(file3)

with open("Datasets/Dataset1/file1.json", "r") as file4:
    json4 = json.load(file4)

with open("Datasets/Dataset1/file1.json", "r") as file5:
    json5 = json.load(file5)

user

json_files = [json1, json2, json3, json4, json5]
for i in range(len(restaurant_data.shape[0])):
    cur_data = restaurant_data.iloc[i]
    res_id1 = cur_data["Restaurant ID"]
    combined_text = None
    for j in json_files:
        for z in range(len(json1)):
            res_data = j[z]["restaurants"]
            for k in range(len(res_data)):
                res_id_m = res_id1["R"]["res_id"]
                if res_id_m == res_id1:
                    user_rating = res_id1["user_rating"]
                    rating_text = user_rating["rating_text"]
                    rating_color = user_rating["rating_color"]
                    votes = user_rating["votes"]
                    aggregate_rating = user_rating["aggregate_rating"]

                    combined_text = rating_text + " " + rating_color + " " + votes + " " + aggregate_rating

    print(combined_text)
