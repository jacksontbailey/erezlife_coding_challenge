from core.config.database import DB_SETTING
from core.challenges.question_1.run_question_1 import run_question_1
from core.challenges.question_2.html_parser import HTMLParser

if __name__ == "__main__":
    #DB_SETTING.delete_tables()
    #all_applications = run_question_1()
    #print(all_applications)

    # Test cases
    html_parser = HTMLParser()

    html1 = "<html><body><div></a></body></html>"
    html2 = "<html><body><div><a></div></a>"
    html3 = "<html><body><div><a></a></div></body></html>"

    #print(html_parser.parse_html(html1))  # Should print an error message
    print(html_parser.parse_html(html2))  # Should print an error message
    print(html_parser.parse_html(html3))  # Should be correct 