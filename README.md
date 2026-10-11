# 💻 Decoding Tech Careers

### Stack Overflow Developer Survey 2025 | Data Analysis & Interactive Dashboard

## Project Overview

This project explores global developer career trends using data from the Stack Overflow Developer Survey 2025.

The objective is to understand how work experience, job roles, countries, education levels, programming technologies, and work arrangements relate to developer compensation.

The project includes exploratory data analysis (EDA), data cleaning, statistical analysis, interactive visualizations, and a Streamlit dashboard.

## Dataset

**Source:** Stack Overflow Developer Survey 2025

- Original dataset: 49,191 respondents
- Cleaned salary dataset: 23,177 records
- Annual compensation measured in USD
- Salary analysis range: $1,000–$1,000,000

## Key Research Questions

1. How does work experience relate to developer salaries?
2. Which developer roles report the highest compensation?
3. Which countries have the highest median developer salaries?
4. What are the most commonly used programming languages and technologies?
5. How does education level relate to compensation?
6. How do remote, hybrid, and in-person salaries compare?

## Technologies Used

- **Python** — Data analysis
- **Pandas** — Data cleaning and manipulation
- **Plotly** — Interactive visualizations
- **SciPy** — Statistical analysis
- **Jupyter Notebook** — Exploratory data analysis
- **Streamlit** — Interactive dashboard

## Key Findings

- Work experience has a moderate positive association with annual compensation (Spearman correlation = 0.44).
- Senior executives and engineering managers report some of the highest median salaries.
- The United States, Switzerland, and Israel lead the salary comparison among countries with at least 100 salary responses.
- JavaScript, HTML/CSS, SQL, and Python are among the most commonly reported technologies.
- Remote respondents report higher median compensation than in-person respondents in the overall sample.

## Dashboard Features

The interactive dashboard includes:

- Country selection filter
- Salary overview metrics
- Salary vs. work experience
- Salary by job role
- Salary by country
- Most popular programming languages and technologies
- Salary by education level
- Salary by work arrangement
- Key findings and methodology

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch the dashboard:

```bash
streamlit run app.py
```

## Project Limitations

The survey is based on self-reported responses and is not representative of all developers worldwide. Salary differences may be influenced by location, seniority, occupation, and other factors. Correlation does not imply causation.

## Data Source

[Stack Overflow Developer Survey](https://survey.stackoverflow.co/)

## Author

Computer Science Student | Data Science & Analytics