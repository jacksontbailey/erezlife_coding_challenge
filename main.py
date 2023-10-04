from core.config.database import DB_SETTING
from core.challenges.question_1.student_applications import get_student_applications

if __name__ == "__main__":
    DB_SETTING.delete_tables()
    DB_SETTING.create_tables()
    DB_SETTING.add_dummy_data()
    all_applications = get_student_applications()
    print(all_applications)