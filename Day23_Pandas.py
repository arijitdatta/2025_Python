import pandas as pd

#People : Alice, Bob, Charlie
#Age : 24, 27, 22
#City : New York, Los Angeles, Chicago

#Define a dictionary with the data
data = {
    'People': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

#Create a DataFrame from the dictionary
df = pd.DataFrame(data)
print(df)


#Uploading a xlsx file
df_excel = pd.read_excel('Day23_student_scores.xlsx')
print(df_excel)

#uploading a json file
df_json = pd.read_json('Day23_student_scores.json')
print(df_json)

#Uploading a nested_json file
df_nested_json = pd.read_json('Day23_student_scores_nested.json')
print(df_nested_json)

#Exporting from json to excel
df_json.to_excel('Day23_student_scores_from_json.xlsx', index=False)

#Slicing and dicing the data
print(df["People"]) #Get a column

#Calculate the mean score of subject1
print(df_excel["Subject_1"].mean()) #Get the mean of a column

#Filtering the data
print(df_excel[df_excel["Subject_1"] > 80]) #Get rows where Subject_1 score is greater than 80

#Filtering with multiple conditions
print(df_excel[(df_excel["Subject_1"] > 80) & (df_excel["Subject_2"] > 80)]["Student"]) #Get names of students who scored more than 80 in both subjects