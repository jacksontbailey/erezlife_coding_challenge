from core.config.database import DB_SETTING
from core.challenges.question_1.run_question_1 import run_question_1

if __name__ == "__main__":
    DB_SETTING.delete_tables()
    all_applications = run_question_1()
    print(all_applications)