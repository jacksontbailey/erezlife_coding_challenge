from core.config.database import DB_SETTING
from core.challenges.question_1.student_applications import get_student_applications

def run_question_1():
    # Create tables and add dummy data
    DB_SETTING.create_tables()
    DB_SETTING.add_dummy_data()

    # Retrieve all applications for students
    all_applications = get_student_applications()

    return all_applications

if __name__ == "__main__":
    all_applications = run_question_1()
    print(all_applications)
