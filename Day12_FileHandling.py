#Reading from a file
with open('Day12_TextFileSample.txt', 'r') as file:
    print(file.read())
    file.close()

#Appending to a file
with open('Day12_TextFileSample.txt', 'a') as file:
    file.write("\nAppending this line to the file.")
    file.close()
with open('Day12_TextFileSample.txt', 'r') as file:
    print(file.read())
    file.close()

print("--------------------------------------------------")

#Working with csv files
import pandas as pd #This line initially gave error as pandas was unknown - fixed by executing - pip install pandas 

#Reading a csv file
df = pd.read_csv('Day12_CSVFileSample.csv')
print(df)

#Appending to a csv file
#new_data = {'Column1': ['Value1'], 'Column2': ['Value2']}
#df = df.append(pd.DataFrame(new_data), ignore_index=True)
#df.to_csv('Day12_CSVFileSample.csv', index=False)
