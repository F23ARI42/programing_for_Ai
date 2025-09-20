import pandas as pd
data=pd.read_csv("StudentsPerformance.csv")
print(data)
math_mean=data["math score"].mean()
read_mean=data["reading score"].mean()
write_mean=data["writing score"].mean()
#print(math_mean,read_mean,write_mean)
#print(f"math_score,{(data["math score"]>=50).sum()},reading score,{(data["reading score"]>=50).sum()},writing score",{(data["writing score"]>=50).sum()})
score=data["reading score"],data["math score"],data["writing score"].sum()
female = data[data['gender'] == 'female']
male = data[data['gender'] == 'male']
male_score=male["reading score"].mean()+male["math score"].mean()+male["writing score"].mean()
female_score=female["reading score"].mean()+female["math score"].mean()+female["writing score"].mean()
print(male_score)
print(female_score)
differnce=female_score-male_score
print("differnce",differnce)
if differnce>10 or differnce<-10:
    print("there is significant difference")
else:
    print("there is no significant difference")
parental_education=data.groupby("parental level of education")[["math score","reading score","writing score"]].mean()
print(parental_education)
course_level=data.groupby("test preparation course")[["math score","reading score","writing score"]].mean()
print(course_level)
sum_score={
"sum_math_score":data["math score"].sum(),
"sum_reading_score":data["reading score"].sum(),
"sum_writing_score":data["writing score"].sum()}
max_subject = max(sum_score, key=sum_score.get)
min_subject = min(sum_score, key=sum_score.get)
print(f"Highest total score: {max_subject} ({sum_score[max_subject]})")
print(f"Lowest total score: {min_subject} ({sum_score[min_subject]})")
correlation=data["math score"].corr(data["reading score"])
print(correlation)
correlation=data["reading score"].corr(data["writing score"])
print(correlation)