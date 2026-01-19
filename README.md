# Pakistan Job Market Analysis
  The primary objective of this project is to provide a data-driven look at employment trends in Pakistanusing a real-world dataset from Rozee.pk. By using  **Python**, **Pandas**, and **Streamlit**, this dashboard allows users to filter through 1,000+ job postings to find meaningful career insights.
The project focuses on applying Exploratory Data Analysis (EDA) and developing an interactive dashboard to extract meaningful insights about jobs across cities, experience levels, salaries, job types, functional areas, and skills.

### Key Questions Answered:
* Which cities are the main hubs for employment?
* How does salary scale with years of experience in different sectors?
* What are the top 10 skills required by employers today?
* What is the distribution of job types (Full-time vs. Part-time) across functional areas?

## Dataset Features
* **Source:** [Kaggle - Pakistan Job Market Dataset](https://www.kaggle.com/datasets/zincly/pakistan-job-market-dataset-rozee-pk)
* **Size:** 1,000+ job postings.
* **Attributes:** Job Title, City, Salary, Experience Level, Job Type, Education, Functional Area, and Required Skills.

## Data Cleaning Highlights
To ensure accuracy, the following preprocessing steps were performed:
1. **Salary Normalization:** Used Regex to convert range strings (e.g., "PKR 30k-60k") into numeric mean values.
2. **City Extraction:** Cleaned messy location strings to isolate 17 distinct Pakistani cities.
3. **Experience Mapping:** Derived categorical levels (Entry, Junior, Mid, Senior) from raw numeric years.
4. **Skill Tokenization:** Normalized and exploded the skills column for granular analysis.

##  Features of the Dashboard
* **KPI Overview:**Real-time counters for Total Jobs, Functional Areas, and Cities covered.
* **City Analytics:** Bar charts showing job density by region (Lahore, Karachi, and Islamabad leading).
* **Salary vs. Experience:** A scatter plot to visualize the correlation between career growth and pay.
* **Skill Demand Heatmap:** Dynamic bar charts that update based on the selected functional area.


### Key Metrics
* **Total Jobs Analyzed:** 1,034
* **Cities Covered:** 17
* **Unique Job Titles:** 704
* **Functional Areas:** 48

## Visual Insights (Dashboard Gallery)

### 1. Main Dashboard & KPIs
The landing page provides a high-level summary of the job market landscape.
![Main Dashboard Screenshot](https://github.com/HafzaBatool-ML/Pakistan-Job-Market-Analysis/blob/main/Dash%20board%20Home%20page.jpeg)

### 2. Job Distribution by City
Lahore, Karachi, and Islamabad represent the "Golden Triangle" of employment in Pakistan, holding the vast majority of opportunities.

### 3. Salary vs. Experience Correlation
Data shows a clear upward trajectory in PKR as experience increases, with Senior roles commanding nearly 3x the salary of Entry-level positions.


### 4. Top Skills by Industry
The dashboard dynamically filters skills based on the functional area (e.g., Python for IT, Negotiation for Sales).


## Tech Stack & Methodology
* **Language:** Python 3.x
* **Libraries:** Pandas (Data Cleaning), Plotly (Interactive Charts), Streamlit (Dashboard Framework), Seaborn/Matplotlib (Static EDA).
* **Cleaning Process:** Handled null values, standardized 17 city names via Regex, and converted complex salary strings (e.g., "30k-60k") into numeric averages for calculation.

---
**Developed by:** Hafza Batool  
**Namal University Mianwali** | Department of Mathematics  
**Supervisor:** Mr. Muhammad Bilal
