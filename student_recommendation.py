import csv
import pandas as pd

def getindex(unique_id):
    with open('students_data.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for index, row in enumerate(reader):
            if row['unique_id'].strip() == unique_id.strip():
                return index
                

def studentrec(unique_id):
    index = getindex(unique_id)
    print(index)
    ids = find_ids(index)
    return ids
        
        
        
def find_ids(index):
    df = pd.read_csv('recomendation_student.csv')
    df1 = pd.read_csv('students_data.csv')
    print(index, df.index)
    if index in df.index:
        row_values = df.loc[index].values.tolist() 
        id = []
        for i in row_values:
            unique_index = df1.iloc[i]['unique_id']
            name = df1.iloc[i]['Name']
            id.append((name, unique_index))
    return id

def findprofile(id):
    pass
             
    
    


    
    