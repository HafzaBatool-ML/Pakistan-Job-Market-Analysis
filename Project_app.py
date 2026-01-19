import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------
# Load Dataset
df = pd.read_csv("RozeePk-2024.csv")

# ------------------------------
# Streamlit Page Config
st.set_page_config(
    page_title="Pakistan Job Market Dashboard",
    layout="wide",
    initial_sidebar_state= "expanded"
)

# ------------------------------
st.title("Pakistan Job Market Insights Dashboard")

# ------------------------------
# Sidebar Filters
st.sidebar.header("Filters")

# Job Type Filter (for city chart)
job_type_options = ["None"] + df["Job Type"].unique().tolist()
selected_job_type = st.sidebar.selectbox("Select Job Type (City-wise Jobs)", job_type_options)

# Functional Area Filter (for salary and skills)
functional_area_options = ["All"] + df["functional_area"].unique().tolist()
selected_functional_area = st.sidebar.selectbox("Select Functional Area", functional_area_options)

# City Filter (for salary scatter)
city_options = ["All"] + df["City"].unique().tolist()
selected_cities = st.sidebar.multiselect("Select Cities (Salary Scatter)", city_options, default=["All"])

# Job Title Filter (for experience vs job type)
job_title_options = ["All"] + df["title"].unique().tolist()
selected_job_title = st.sidebar.selectbox("Select Job Title (Experience vs Job Type)", job_title_options)

# ------------------------------
# KPI Cards
total_jobs = len(df)
avg_salary = df["functional_area"].nunique()
unique_cities = df["City"].nunique()
unique_skills =  df["title"].nunique()
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Jobs", total_jobs)
col2.metric("Functional Areas", avg_salary)
col3.metric("Cities Covered", unique_cities)
col4.metric("Unique Job Title", unique_skills)

# ------------------------------
# 1. Cities with Highest Number of Job Postings
st.subheader("1. Job Postings by City")
city_df = df.copy()
if selected_job_type != "None":
    city_df = city_df[city_df["Job Type"] == selected_job_type]

city_count = city_df["City"].value_counts().reset_index()
city_count.columns = ["City", "Number of Jobs"]
fig1 = px.bar(city_count, x="City", y="Number of Jobs", text="Number of Jobs",)
st.plotly_chart(fig1, use_container_width=True)

# ------------------------------
# 2. Salary vs Experience Scatter
st.subheader("2. Salary Ranges by Experience and Functional Area")
salary_df = df.copy()
if "All" not in selected_cities:
    salary_df = salary_df[salary_df["City"].isin(selected_cities)]
if selected_functional_area != "All":
    salary_df = salary_df[salary_df["functional_area"] == selected_functional_area]


salary_df["Experience_Capped"] = salary_df["Experience"].clip(lower=0, upper=10)

fig2 = px.scatter(
    salary_df,
    x="Experience_Capped",
    y="Salary",
    color="experience_level",
    hover_data=["title", "City","functional_area"],
    labels={"Experience_Capped": "Experience (Years)"},
    title="Salary vs Experience"
)
st.plotly_chart(fig2, use_container_width=True)


# ------------------------------
# 3. Most Demanded Skills by Functional Area
st.subheader("3. Most In-Demand Skills")
skills_df = df.copy()
if selected_functional_area != "All":
    skills_df = skills_df[skills_df["functional_area"] == selected_functional_area]

# Explode skills column
skills_df = skills_df.assign(skill=skills_df["skills"].str.split(",")).explode("skill")
skills_df["skill"] = skills_df["skill"].str.strip().str.lower()
top_skills = skills_df.groupby("skill").size().reset_index(name="Count").sort_values("Count", ascending=False).head(10)

fig3 = px.bar(top_skills, x="skill", y="Count", text="Count", title="Top 10 Skills")
st.plotly_chart(fig3, use_container_width=True)

# ------------------------------
# 4. Experience Level vs Job Titles
st.subheader("4. Experience Level vs Job Posting Count")
exp_df = df.copy()
if selected_job_title != "All":
    exp_df = exp_df[exp_df["title"] == selected_job_title]

exp_count = exp_df.groupby("experience_level").size().reset_index(name="Count")
fig4 = px.bar(exp_count, x="experience_level", y="Count", text="Count", color="experience_level")
st.plotly_chart(fig4, use_container_width=True)
