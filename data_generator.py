
import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()

np.random.seed(42)

COURSES = [
    "Python Programming",
    "Machine Learning",
    "Data Science",
    "Cyber Security",
    "Cloud Computing",
    "Web Development"
]


def generate_realistic_dataset(num_students=5000):

    students = []

    for i in range(num_students):

        student_id = f"STU{i+1:05d}"

        name = fake.name()

        age = np.random.randint(18, 30)

        course = np.random.choice(COURSES)

        learner_type = np.random.choice(
            ["high", "medium", "low"],
            p=[0.3, 0.5, 0.2]
        )

        # HIGH ENGAGEMENT STUDENTS
        if learner_type == "high":

            login_frequency = np.random.randint(20, 30)

            videos_watched = np.random.randint(70, 100)

            avg_watch_time = np.random.randint(60, 120)

            assignments_completed = np.random.randint(8, 10)

            assignment_delay_days = np.random.randint(0, 2)

            quiz_attempts = np.random.randint(8, 12)

            attendance_rate = np.random.randint(85, 100)

            study_hours_weekly = np.random.randint(20, 35)

            inactivity_days = np.random.randint(0, 2)

            forum_participation = np.random.randint(10, 25)

        # MEDIUM ENGAGEMENT STUDENTS
        elif learner_type == "medium":

            login_frequency = np.random.randint(10, 20)

            videos_watched = np.random.randint(40, 70)

            avg_watch_time = np.random.randint(30, 60)

            assignments_completed = np.random.randint(4, 8)

            assignment_delay_days = np.random.randint(2, 6)

            quiz_attempts = np.random.randint(4, 8)

            attendance_rate = np.random.randint(60, 85)

            study_hours_weekly = np.random.randint(8, 20)

            inactivity_days = np.random.randint(2, 7)

            forum_participation = np.random.randint(3, 10)

        # LOW ENGAGEMENT STUDENTS
        else:

            login_frequency = np.random.randint(1, 10)

            videos_watched = np.random.randint(5, 40)

            avg_watch_time = np.random.randint(5, 30)

            assignments_completed = np.random.randint(0, 4)

            assignment_delay_days = np.random.randint(6, 15)

            quiz_attempts = np.random.randint(0, 4)

            attendance_rate = np.random.randint(20, 60)

            study_hours_weekly = np.random.randint(1, 8)

            inactivity_days = np.random.randint(7, 20)

            forum_participation = np.random.randint(0, 3)

        # REALISTIC ENGAGEMENT SCORE
        engagement_score = (
            login_frequency * 0.15 +
            videos_watched * 0.20 +
            avg_watch_time * 0.10 +
            assignments_completed * 5 +
            attendance_rate * 0.20 +
            study_hours_weekly * 0.20
        )

        # REALISTIC QUIZ SCORE
        avg_quiz_score = min(
            100,
            max(
                20,
                int(
                    engagement_score * 0.6 +
                    np.random.normal(15, 8)
                )
            )
        )

        # COURSE COMPLETION
        course_completion = min(
            100,
            max(
                5,
                int(
                    engagement_score * 0.8
                )
            )
        )

        students.append([
            student_id,
            name,
            age,
            course,
            login_frequency,
            videos_watched,
            avg_watch_time,
            assignments_completed,
            assignment_delay_days,
            quiz_attempts,
            avg_quiz_score,
            forum_participation,
            attendance_rate,
            inactivity_days,
            study_hours_weekly,
            course_completion
        ])

    columns = [
        "student_id",
        "name",
        "age",
        "course",
        "login_frequency",
        "videos_watched",
        "avg_watch_time",
        "assignments_completed",
        "assignment_delay_days",
        "quiz_attempts",
        "avg_quiz_score",
        "forum_participation",
        "attendance_rate",
        "inactivity_days",
        "study_hours_weekly",
        "course_completion"
    ]

    # CREATE DATAFRAME HERE
    df = pd.DataFrame(students, columns=columns)

    return df


if __name__ == "__main__":

    df = generate_realistic_dataset()

    df.to_csv("realistic_student_data.csv", index=False)

    print("Dataset generated successfully!")

