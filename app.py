
import streamlit as st
import pandas as pd
import plotly.express as px

from data_generator import generate_realistic_dataset
from feature_engineering import create_intelligence_features
from risk_engine import classify_risk
from recommendation_engine import generate_recommendations


# PAGE CONFIG
st.set_page_config(
    page_title="EduInsight AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# CUSTOM CSS
st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
        color: white;
    }

    .stMetric {
        background-color: #1E1E1E;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #333333;
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    h1, h2, h3, h4 {
        color: white;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# LOAD DATA
@st.cache_data
def load_data():

    df = generate_realistic_dataset(5000)

    df = create_intelligence_features(df)

    df = classify_risk(df)

    df = generate_recommendations(df)

    return df


# DATAFRAME
df = load_data()


# SIDEBAR
st.sidebar.title("🎓 EduInsight AI")

st.sidebar.markdown(
    "AI-Powered Educational Intelligence Platform"
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Student Insights",
        "Risk Center",
        "Recommendations"
    ]
)


# COURSE FILTER
selected_course = st.sidebar.selectbox(
    "Select Course",
    ["All Courses"] + list(df["course"].unique())
)


# FILTER DATA
if selected_course != "All Courses":

    df = df[df["course"] == selected_course]


# DASHBOARD
if menu == "Dashboard":

    st.title("📊 AI Educational Analytics Dashboard")

    st.markdown(
        "Real-time student engagement and risk intelligence system"
    )

    # KPI CARDS
    total_students = len(df)

    active_students = len(
        df[df["attendance_rate"] > 75]
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
        "🎓 Total Students",
        total_students
    )

    col2.metric(
        "✅ Active Learners",
        active_students
    )

    col3.metric(
        "⚠ High Risk Students",
        high_risk_students
    )

    col4.metric(
        "📈 Average Quiz Score",
        avg_score
    )

    st.markdown("---")

    # ALERT SECTION
    if high_risk_students > 0:

        st.error(
            f"⚠ ALERT: {high_risk_students} students are at HIGH academic risk"
        )

    # CHARTS
    col5, col6 = st.columns(2)

    with col5:

        st.subheader("Risk Distribution")

        risk_chart = px.pie(
            df,
            names="risk_level",
            hole=0.4,
            title="Student Risk Categories"
        )

        st.plotly_chart(
            risk_chart,
            use_container_width=True
        )

    with col6:

        st.subheader("Course Completion Distribution")

        completion_chart = px.histogram(
            df,
            x="course_completion",
            nbins=20,
            title="Course Completion"
        )

        st.plotly_chart(
            completion_chart,
            use_container_width=True
        )

    st.markdown("---")

    # ENGAGEMENT VS PERFORMANCE
    st.subheader("📈 Engagement vs Quiz Performance")

    scatter_chart = px.scatter(
        df,
        x="engagement_score",
        y="avg_quiz_score",
        color="risk_level",
        size="study_hours_weekly",
        hover_data=["student_id", "name", "course"],
        title="Student Engagement Analytics"
    )

    st.plotly_chart(
        scatter_chart,
        use_container_width=True
    )

    # TOP PERFORMERS
    st.subheader("🏆 Top Performing Students")

    top_students = df.sort_values(
        by="avg_quiz_score",
        ascending=False
    ).head(10)

    st.dataframe(top_students)


# STUDENT INSIGHTS
elif menu == "Student Insights":

    st.title("👨‍🎓 Student Intelligence Insights")

    student_search = st.text_input(
        "Enter Student ID"
    )

    if student_search:

        student_data = df[
            df["student_id"] == student_search
        ]

        if not student_data.empty:

            row = student_data.iloc[0]

            st.subheader(f"Student Profile: {row['name']}")

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "Quiz Score",
                row['avg_quiz_score']
            )

            col2.metric(
                "Attendance",
                row['attendance_rate']
            )

            col3.metric(
                "Risk Level",
                row['risk_level']
            )

            st.progress(int(row['course_completion']))

            st.info(row['recommendation'])

            st.dataframe(student_data)

        else:

            st.error("Student not found")


# RISK CENTER
elif menu == "Risk Center":

    st.title("⚠ Student Risk Monitoring Center")

    high_risk = df[
        df["risk_level"] == "High Risk"
    ]

    medium_risk = df[
        df["risk_level"] == "Medium Risk"
    ]

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🚨 High Risk Students")

        st.dataframe(high_risk)

    with col2:

        st.subheader("⚡ Medium Risk Students")

        st.dataframe(medium_risk)

    st.subheader("📢 AI Alerts")

    for _, row in high_risk.head(10).iterrows():

        st.warning(
            f"{row['student_id']} - {row['name']} has poor attendance and low academic performance"
        )


# RECOMMENDATIONS
elif menu == "Recommendations":

    st.title("🤖 Personalized Learning Recommendations")

    recommendation_df = df[[
        "student_id",
        "name",
        "course",
        "risk_level",
        "recommendation"
    ]]

    st.dataframe(recommendation_df)

    st.subheader("🎯 AI Suggested Interventions")

    for _, row in recommendation_df.head(15).iterrows():

        st.info(
            f"{row['student_id']} | {row['name']} → {row['recommendation']}"
        )


# FOOTER
st.markdown("---")

st.markdown(
    "### EduInsight AI — Educational Intelligence & Risk Analytics Platform"
)
