import pandas as pd



def create_intelligence_features(df):

    # Engagement Score
    df["engagement_score"] = (
        df["login_frequency"] * 0.20 +
        df["videos_watched"] * 0.20 +
        df["assignments_completed"] * 5 +
        df["attendance_rate"] * 0.20 +
        df["study_hours_weekly"] * 0.20
    )
    
    # Consistency Score
    df["consistency_score"] = (
        df["attendance_rate"] * 0.5 +
        (30 - df["inactivity_days"]) * 1.5
    )

    # Procrastination Index
    df["procrastination_index"] = (
        df["assignment_delay_days"] * 5
    )

    # Risk Score
    df["risk_score"] = (
        df["inactivity_days"] * 2 +
        df["assignment_delay_days"] * 3 +
        (100 - df["attendance_rate"]) * 0.5 +
        (100 - df["avg_quiz_score"]) * 0.4
    )

    return df



