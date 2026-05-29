import pandas as pd



def classify_risk(df):

    risk_levels = []

    for _, row in df.iterrows():

        if (
            row["attendance_rate"] < 40 and
            row["avg_quiz_score"] < 45
        ):
            risk_levels.append("High Risk")

        elif (
            row["attendance_rate"] < 70 or
            row["avg_quiz_score"] < 60
        ):
            risk_levels.append("Medium Risk")

        else:
            risk_levels.append("Low Risk")

    df["risk_level"] = risk_levels

    return df