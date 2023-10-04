from core.config.database import DB_SETTING
from core.challenges.question_1.run_question_1 import run_question_1
from core.challenges.question_2.html_parser import HTMLParser
from core.challenges.question_3.nested_structure_generator import generate_nested_structure
from core.challenges.question_4.process_shapes import process_shapes


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
    #print(html_parser.parse_html(html2))  # Should print an error message
    #print(html_parser.parse_html(html3))  # Should be correct

    # Example usage
    #letters = ['a', 'b', 'c', 'd', 'e', 'f']
    #nested_structure = generate_nested_structure(letters)
    #print(nested_structure)

    file_location = "core\challenges\question_4"
    input_file = f"{file_location}\shapes.csv"
    output_file = f"{file_location}\output.csv"
    process_shapes(input_file, output_file)