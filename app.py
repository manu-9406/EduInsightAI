import streamlit as st
import pandas as pd
import plotly.express as px

from data_generator import generate_realistic_dataset
from feature_engineering import create_intelligence_features
from risk_engine import classify_risk
from recommendation_engine import generate_recommendations


st.set_page_config(
    page_title="EduInsight AI",
    layout="wide"
)


# Sidebar
st.sidebar.title("EduInsight AI")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Student Insights",
        "Risk Center",
                "Recommendations"
    ]
)


# Generate Dataset
@st.cache_data

def load_data():

    df = generate_realistic_dataset(5000)

    df = create_intelligence_features(df)

    df = classify_risk(df)

    df = generate_recommendations(df)

    return df
# Load Data

df = load_data()


# DASHBOARD
if menu == "Dashboard":

    st.title("AI-Powered Educational Intelligence Dashboard")

    total_students = len(df)

    active_students = len(
        df[df["attendance_rate"] > 70]
    )

    high_risk_students = len(
        df[df["risk_level"] == "High Risk"]
    )

    avg_score = round(
        df["avg_quiz_score"].mean(),
        2
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(
        "Total Students",
        total_students
    )

    col2.metric(
        "Active Learners",
        active_students
    )

    col3.metric(
        "High Risk Students",
        high_risk_students
    )

    col4.metric(
        "Average Quiz Score",
        avg_score
    )


    st.subheader("Risk Distribution")

    risk_chart = px.pie(
        df,
        names="risk_level",
        title="Student Risk Levels"
        )

    st.plotly_chart(
        risk_chart,
        use_container_width=True
    )


    st.subheader("Engagement vs Quiz Performance")

    scatter_chart = px.scatter(
        df,
        x="engagement_score",
        y="avg_quiz_score",
        color="risk_level",
        hover_data=["student_id", "name"],
        title="Engagement vs Performance"
    )

    st.plotly_chart(
        scatter_chart,
        use_container_width=True
    )


    st.subheader("Course Completion Analysis")

    completion_chart = px.histogram(
df,
        x="course_completion",
        nbins=20,
        title="Course Completion Distribution"
    )

    st.plotly_chart(
        completion_chart,
        use_container_width=True
    )


# STUDENT INSIGHTS
elif menu == "Student Insights":

    st.title("Student Intelligence Insights")

    student_search = st.text_input(
        "Enter Student ID"
    )

    if student_search:

        student_data = df[
            df["student_id"] == student_search
        ]

        if not student_data.empty:

            st.dataframe(student_data)
        else:

            st.error("Student not found")


    st.subheader("Top Performing Students")

    top_students = df.sort_values(
        by="avg_quiz_score",
        ascending=False
    ).head(10)

    st.dataframe(top_students)


# RISK CENTER
elif menu == "Risk Center":

    st.title("Student Risk Monitoring Center")

    high_risk = df[
        df["risk_level"] == "High Risk"
    ]

    st.subheader("High Risk Students")
    st.dataframe(high_risk)


    st.subheader("High Risk Alerts")

    for _, row in high_risk.head(10).iterrows():

        st.warning(
            f"{row['student_id']} - {row['name']} is at HIGH RISK due to poor attendance and low quiz performance"
        )


# RECOMMENDATIONS
elif menu == "Recommendations":

    st.title("Personalized Learning Recommendations")

    recommendation_df = df[[
        "student_id",
        "name",
        "risk_level",
        "recommendation"
    ]]
    st.dataframe(recommendation_df)


    st.subheader("Sample AI Recommendations")

    for _, row in recommendation_df.head(10).iterrows():

        st.info(
            f"{row['student_id']} → {row['recommendation']}"
        )