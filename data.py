import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt
df=pd.read_csv("StudentsPerformance.csv")
# print(df.head())
# df.info()
# print(df.describe())
# print(df.shape)
# print(df.isna())
# print(df.isna().sum())
#print(df.duplicated().sum())
# print(df.columns)

# ---- Outliers Detection ----
print("----Outliers----")
subjects = ["math score", "reading score", "writing score"]
for subject in subjects:
    Q1 = df[subject].quantile(0.25)
    Q3 = df[subject].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[subject] < lower_limit) |
        (df[subject] > upper_limit)
    ]

    print(f"\n{subject}")
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))
# ----Average score of each subject----

subjects=["math score","reading score","writing score"]
print("-Average score of each subject-")
print(df[subjects].mean())
df["average score"]=df[subjects].mean(axis=1)
print("-Average scire of each student-")
print(df["average score"].head())

# ---- overall Average Score of Students ----
overall_average=df["average score"].mean()
print("----overall Average Score----")
print(overall_average)

# ---- min score of each subject ----
minimum_marks = df[subjects].min()
print("---- min score of each subject ----")
print(minimum_marks)

# ---- max score of each subject ----
maximum_marks = df[subjects].max()
print("---- max score of each subject ----")
print(maximum_marks)

# ---- Total Marks of each student ----
df["total marks"]=df[subjects].sum(axis=1)
print("---- Total Marks of each student ----")
print(df["total marks"].head())

# ---- overall min total score ----
overall_minimum_score = df["total marks"].min()
print("---- overall min total score ----")
print(overall_minimum_score)

# ---- overall max total score ----
overall_maximum_score= df["total marks"].max()
print("---- overall max total score ----")
print(overall_maximum_score)

# ---- display student info who has min total score ----
lowest_score_student = df.loc[df["total marks"].idxmin()]
print("----lowest_score_student----")
print(lowest_score_student)

# ---- display student info who has max total score ----
highest_score_student = df.loc[df["total marks"].idxmax()]
print("----highest_score_student----")
print(highest_score_student)

# ----Gender analysis----
gender_analysis=df.groupby("gender")[subjects].mean()
print(" ----Gender analysis----")
print(gender_analysis)

# ----Test preparation analysis ----
test_prep_analysis=df.groupby("test preparation course")[subjects].mean()
print("----Test preparation analysis ----")
print(test_prep_analysis)

# ---- Parental Education Analysis  ----
parent_edu_anlsys=df.groupby("parental level of education")[subjects].mean()
print("---- Parental Education Analysis  ----")
print(parent_edu_anlsys)

# ---- Data Visualization ----

#---- Gender Analysis Graph ----
gender_analysis.T.plot(kind="bar")
plt.title("Gender-wise Subject Performance")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.legend(title="Subject")
plt.show()

# ----Test preperation Graph ----
test_prep_analysis.T.plot(kind="bar")
plt.title("Test Preparation Course-wise Performance")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.legend(title="Test Preparation")
plt.show()

# ---- Parental Eduction Analysis Graph ----
parent_edu_anlsys.plot(kind="bar")
plt.title("Performance by Parental Education Level")
plt.xlabel("Parental Education Level")
plt.ylabel("Average Score")
plt.legend(title="Subject")
plt.xticks(rotation=45)
plt.show()