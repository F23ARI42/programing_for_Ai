import pandas as pd
my_dict={"name":{0:"Alice",1:"Bob",2:"Carol",3:"David",4:"Eve"},"Age":{0:20,1:22,2:21,3:23,4:22},"Department":{0:"AI",1:"CS",2:"Data Sci",3:"IT",4:"AI"},"GPA":{0:3.8,1:3.5,2:3.9 ,3:3.7,4:3.6}}
df = pd.DataFrame(my_dict)
df["Graduation Year"]=[24,24,24,24,24]
#print(df[df["Department"]=="AI"])
print(df)



