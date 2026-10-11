import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Decoding Tech Careers",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Decoding Tech Careers")

st.write(
    "Exploring developer salaries, experience, job roles, "
    "and career trends using the Stack Overflow Developer Survey 2025."
)

df = pd.read_csv("cleaned_salary_data.csv")

# Country Filter
st.sidebar.header("🔎 Filters")

countries = sorted(df["Country"].dropna().unique())

selected_country = st.sidebar.selectbox(
    "Select Country",
    ["All Countries"] + countries
)

if selected_country == "All Countries":
    filtered_df = df.copy()
else:
    filtered_df = df[df["Country"] == selected_country].copy()


st.subheader("📊 Salary Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Salary Records",
        f"{len(filtered_df):,}"
    )

with col2:
    st.metric(
        "Median Annual Salary",
        f"${filtered_df['ConvertedCompYearly'].median():,.0f}"
    )

with col3:
    st.metric(
        "Average Annual Salary",
        f"${filtered_df['ConvertedCompYearly'].mean():,.0f}"
    )

with col4:
    st.metric(
        "Countries Represented",
        filtered_df["Country"].nunique()
    )

st.divider()

st.subheader("Dataset Preview")
st.dataframe(filtered_df.head(), use_container_width=True)

# Salary vs Work Experience
st.subheader("📈 Salary vs Work Experience")

experience_data = filtered_df.dropna(subset=["WorkExp"])

experience_salary = (
    experience_data.groupby("WorkExp")["ConvertedCompYearly"]
    .median()
    .reset_index()
    .sort_values("WorkExp")
)

fig_experience = px.line(
    experience_salary,
    x="WorkExp",
    y="ConvertedCompYearly",
    markers=True,
    title="Median Annual Salary by Work Experience",
    labels={
        "WorkExp": "Years of Work Experience",
        "ConvertedCompYearly": "Median Annual Salary (USD)"
    }
)

st.plotly_chart(fig_experience, use_container_width=True)


# Salary by Job Role
st.subheader("💼 Salary by Job Role")

role_data = filtered_df.dropna(subset=["DevType"])

role_salary = (
    role_data.groupby("DevType")["ConvertedCompYearly"]
    .agg(["median", "count"])
    .reset_index()
)

# Exclude roles with fewer than 30 respondents
role_salary = role_salary[role_salary["count"] >= 30]

top_roles = role_salary.nlargest(10, "median")

if not top_roles.empty:
    fig_roles = px.bar(
        top_roles,
        x="median",
        y="DevType",
        orientation="h",
        title="Top 10 Job Roles by Median Annual Salary",
        labels={
            "median": "Median Annual Salary (USD)",
            "DevType": "Job Role"
        },
        hover_data=["count"]
    )

    fig_roles.update_layout(
        yaxis={"categoryorder": "total ascending"},
        height=550
    )

    st.plotly_chart(fig_roles, use_container_width=True)
else:
    st.info("Not enough salary responses for this country.")


    # Salary by Country
st.subheader("🌍 Salary by Country")

country_salary = (
    df.dropna(subset=["Country"])
    .groupby("Country")["ConvertedCompYearly"]
    .agg(["median", "count"])
    .reset_index()
)

# Keep countries with at least 100 salary responses
country_salary = country_salary[
    country_salary["count"] >= 100
]

top_countries = country_salary.nlargest(15, "median")

fig_countries = px.bar(
    top_countries,
    x="median",
    y="Country",
    orientation="h",
    title="Top 15 Countries by Median Annual Salary",
    labels={
        "median": "Median Annual Salary (USD)",
        "Country": "Country"
    },
    hover_data=["count"],
    text="median"
)

fig_countries.update_traces(
    texttemplate="$%{text:,.0f}",
    textposition="outside"
)

fig_countries.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=650,
    margin=dict(l=220)
)

st.plotly_chart(fig_countries, use_container_width=True)



# Most Popular Programming Languages
st.subheader("💻 Most Popular Programming Languages")

languages_df = pd.read_csv("programming_languages.csv")

top_languages = languages_df.head(15)

fig_languages = px.bar(
    top_languages,
    x="Count",
    y="Language",
    orientation="h",
    title="Top 15 Most Popular Programming Languages and Technologies",
    labels={
        "Count": "Number of Respondents",
        "Language": "Language / Technology"
    },
    text="Count"
)

fig_languages.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=600
)

st.plotly_chart(fig_languages, use_container_width=True)

st.caption(
    "Respondents could select multiple technologies. "
    "This chart includes all respondents who answered the language question "
    "and is not affected by the country filter."
)


# Salary by Education Level
st.subheader("🎓 Salary by Education Level")

education_data = filtered_df.dropna(subset=["EdLevel"]).copy()

education_salary = (
    education_data.groupby("EdLevel")["ConvertedCompYearly"]
    .agg(["median", "count"])
    .reset_index()
)

# Shorten education labels for better readability
education_salary["Education"] = education_salary["EdLevel"].apply(
    lambda x: x.split(" (")[0]
)

fig_education = px.bar(
    education_salary,
    x="median",
    y="Education",
    orientation="h",
    title="Median Annual Salary by Education Level",
    labels={
        "median": "Median Annual Salary (USD)",
        "Education": "Education Level"
    },
    hover_data=["count"]
)

fig_education.update_layout(
    yaxis={"categoryorder": "total ascending"},
    height=550
)

st.plotly_chart(fig_education, use_container_width=True)


# Salary by Work Arrangement
st.subheader("🏠 Salary by Work Arrangement")

remote_data = filtered_df.dropna(subset=["RemoteWork"]).copy()

remote_salary = (
    remote_data.groupby("RemoteWork")["ConvertedCompYearly"]
    .agg(["median", "count"])
    .reset_index()
)

# Shorten work arrangement labels
remote_salary["Work Arrangement"] = remote_salary["RemoteWork"].replace({
    "Hybrid (some in-person, leans heavy to flexibility)": "Hybrid - Flexible",
    "Hybrid (some remote, leans heavy to in-person)": "Hybrid - In-person",
    "Your choice (very flexible, you can come in when you want)": "Your Choice"
})

fig_remote = px.bar(
    remote_salary,
    x="Work Arrangement",
    y="median",
    title="Median Annual Salary by Work Arrangement",
    labels={
        "Work Arrangement": "Work Arrangement",
        "median": "Median Annual Salary (USD)"
    },
    text="median",
    hover_data=["count"]
)

fig_remote.update_traces(
    texttemplate="$%{text:,.0f}",
    textposition="outside"
)

fig_remote.update_layout(
    height=500,
    xaxis_tickangle=-20
)

st.plotly_chart(fig_remote, use_container_width=True)


# Key Insights
st.divider()
st.header("🔍 Key Findings")

st.markdown("""
- **Experience:** Work experience has a moderate positive
  association with annual compensation (Spearman = 0.44).

- **Job Roles:** Senior executives and engineering managers
  have the highest median salaries among the analyzed roles.

- **Countries:** The United States, Switzerland, and Israel
  have the highest median salaries among countries with
  at least 100 salary responses.

- **Programming Languages:** JavaScript, HTML/CSS, SQL,
  and Python are the most commonly reported technologies.

- **Education:** Professional degree holders report the
  highest median annual compensation.

- **Remote Work:** Remote respondents report higher median
  salaries than in-person respondents in the overall sample.
""")

# Methodology
st.divider()
st.header("📋 Methodology & Limitations")

with st.expander("View Data Cleaning and Analysis Methods"):
    st.markdown("""
    **Data Source:** Stack Overflow Developer Survey 2025.

    **Original Dataset:** 49,191 respondents.

    **Salary Dataset:** 23,177 records after excluding
    missing annual compensation and applying an exploratory
    salary range of $1,000 to $1,000,000.

    **Salary Metric:** Median annual compensation in USD.

    **Country Comparison:** Countries with fewer than
    100 salary responses were excluded.

    **Statistical Analysis:** Spearman rank correlation
    was used to examine salary and work experience.

    **Limitations:**
    - Survey responses are self-reported.
    - The sample is not representative of all developers.
    - Salary comparisons are not adjusted for cost of living.
    - Associations do not establish causation.
    - Country filtering changes the selected salary analyses;
      global findings above describe the overall sample.
    """)

st.caption(
    "Decoding Tech Careers | Stack Overflow Developer Survey 2025"
)