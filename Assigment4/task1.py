import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("students.csv")
plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Score'], color='purple', alpha=0.6)
plt.title('Relationship Between Age and Score of Students')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()
