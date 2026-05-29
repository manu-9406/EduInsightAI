import pandas as pd



def generate_recommendations(df):

    recommendations = []

    for _, row in df.iterrows():

        recommendation = []

        if row["attendance_rate"] < 50:
            recommendation.append(
                "Increase class attendance"
            )

        if row["avg_quiz_score"] < 50:
            recommendation.append(
                "Practice more quizzes"
            )
        
        if row["assignments_completed"] < 5:
            recommendation.append(
                "Complete pending assignments"
            )

        if row["study_hours_weekly"] < 5:
            recommendation.append(
                "Increase weekly study hours"
            )

        if row["videos_watched"] < 30:
            recommendation.append(
                "Watch more lecture videos"
            )

        if len(recommendation) == 0:
            recommendation.append(
                "Excellent performance. Continue current learning strategy"
            )

        recommendations.append(
            " | ".join(recommendation)
        )

    df["recommendation"] = recommendations

    return df