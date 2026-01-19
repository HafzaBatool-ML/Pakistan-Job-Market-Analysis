
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("RozeePk-2024.csv")

plt.figure(figsize=(10,6))
sns.histplot(df["Salary"], bins=40, kde=True)
plt.title("Salary Distribution with KDE")
plt.xlabel("Salary (PKR)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


plt.figure(figsize=(12,6))
sns.countplot(
    data=df,
    x="City",
    order=df["City"].value_counts().index
)
plt.title("Number of Job Postings by City")
plt.xlabel("City")
plt.ylabel("Job Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

job_type_counts = df["Job Type"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    job_type_counts,
    labels=job_type_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Job Type Distribution")
plt.tight_layout()
plt.show()

from collections import Counter

# Split skills
skills_series = df["skills"].dropna().str.split(",")
skills_list = [skill.strip().lower() for sublist in skills_series for skill in sublist]

top_skills = Counter(skills_list).most_common(10)
skills_df = pd.DataFrame(top_skills, columns=["Skill", "Count"])

plt.figure(figsize=(10,6))
sns.barplot(data=skills_df, x="Count", y="Skill")
plt.title("Top 10 In-Demand Skills")
plt.xlabel("Count")
plt.ylabel("Skill")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10,6))
sns.boxplot(
    data=df,
    x="experience_level",
    y="Salary"
)
plt.title("Salary Distribution by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Salary (PKR)")
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

# Get top functional areas
fa_counts = df["functional_area"].value_counts().head(6)

plt.figure(figsize=(7,7))
plt.pie(
    fa_counts,
    labels=fa_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Distribution of Job Postings by Functional Area (Top 6)")
plt.tight_layout()
plt.show()

