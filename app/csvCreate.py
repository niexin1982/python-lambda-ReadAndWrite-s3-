import csv

header = ['name', 'age','country']
body = [
        ['cherry',50,'japan'], 
        ['strawberry',90,'china'], 
        ['peach',35,'usa'], 
       ]

with open('test.csv', 'w') as f:
 
  writer = csv.writer(f)
  writer.writerow(header)
  writer.writerows(body)

f.close()