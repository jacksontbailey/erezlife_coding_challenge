import pyinputplus as pyip
import re
from core.config.database import DatabaseConfig
from core.challenges.question_2.html_parser import HTMLParser
from core.challenges.question_3.nested_structure_generator import generate_nested_structure
from core.challenges.question_4.process_shapes import process_shapes
from core.challenges.question_1.student_applications import get_student_applications


class QuestionHandler:
    def __init__(self):
        self.db_setting = DatabaseConfig()

    def _get_choice_input(self, options, prompt):
        while True:
            print(prompt)
            for key, value in options.items():
                print(f"{key}: {value}")
            user_choice = pyip.inputChoice(list(options.keys()), prompt='\nEnter the number, letter, or option: ')
            
            selected_option = options[user_choice]
            if selected_option in ['quit', 'go back', 'custom']:
                return selected_option  # Return 'quit', 'go back', or 'custom' to handle outside the loop
            else:
                return selected_option  # Return the selected option if not 'quit', 'go back', or 'custom'

    def run_question_1(self):
        action_options = {
            '1': 'delete tables',
            '2': 'create dataset and tables',
            'b': 'go back',
            'q': 'quit'
        }

        while True:
            action_choice = self._get_choice_input(action_options, prompt='\nSelect an action: ')            
            
            if action_choice == 'delete tables':
                self.db_setting.delete_tables()
                print("\nTables deleted successfully.")
            elif action_choice == 'create dataset and tables':
                number_of_users = pyip.inputInt(prompt='\nEnter the number of users you want to create: ',
                                                min=1, default=5)
                # Create tables and add dummy data
                self.db_setting.create_tables()
                self.db_setting.add_dummy_data(number_of_users)
                # Retrieve all applications for students
                all_applications = get_student_applications()
                print("\nDataset and tables created successfully.")
                print(all_applications)
            elif action_choice == 'go back':
                break
            elif action_choice.lower() == 'quit':
                print("\nExiting the program. Goodbye!")
                exit()
            else:
                print("\nInvalid choice. Please select a valid option.")

    def run_question_2(self):
        html_options = {
            '1': 'html1',
            '2': 'html2',
            '3': 'html3',
            'c': 'custom',
            'b': 'go back',
            'q': 'quit'
        }
        while True:
            html_option = self._get_choice_input(html_options, prompt='\nSelect an HTML option:')            

            if html_option == 'go back':
                break
            elif html_option == 'quit':
                print("\nExiting the program. Goodbye!")
                exit()
            elif html_option == 'custom':
                custom_html = pyip.inputStr(prompt="\nEnter your custom HTML code: ")
                new_html_parser = HTMLParser()  # Create a new instance of HTMLParser
                print(new_html_parser.parse_html(custom_html))
            elif html_option in ['html1', 'html2', 'html3']:
                if html_option == 'html1':
                    html_code = "<html><body><div></a></body></html>"
                elif html_option == 'html2':
                    html_code = "<html><body><div><a></div></a>"
                elif html_option == 'html3':
                    html_code = "<html><body><div><a></a></div></body></html>"
                new_html_parser = HTMLParser()  # Create a new instance of HTMLParser
                print(new_html_parser.parse_html(html_code))
            else:
                print("\nInvalid choice. Please select a valid option.")

    def run_question_3(self):
        use_default = {
            '1': 'yes',
            '2': 'no',
            'b': 'go back',
            'q': 'quit'
        }

        print("\nDefault letters are: ['a', 'b', 'c', 'd', 'e', 'f']")
        while True:
            use_default = self._get_choice_input(use_default, prompt='\nDo you want to use the default list of letters? (yes or no): ')            

            if use_default == 'yes':
                letters = ['a', 'b', 'c', 'd', 'e', 'f']
            elif use_default.lower() == 'quit':
                print("Exiting the program. Goodbye!")
                exit()
            elif use_default.lower() == 'go back':
                break
            else:
                custom_letters = pyip.inputStr(prompt='\nEnter your list of letters: ')
                # Remove non-letter characters and spaces using regular expression
                letters = re.sub(r'[^a-zA-Z]', '', custom_letters)

            nested_structure = generate_nested_structure(letters)
            print(nested_structure)

    def run_question_4(self):
        file_location = "core\\challenges\\question_4"
        input_file = f"{file_location}\\shapes.csv"
        output_file = f"{file_location}\\output.csv"
        process_shapes(input_file, output_file)

    def handle_questions(self):
        action_options = {
            '1': 'question 1',
            '2': 'question 2',
            '3': 'question 3',
            '4': 'question 4',
            'b': 'go back',
            'q': 'quit'
        }

        while True:
            question_choice = self._get_choice_input(action_options, prompt='\nSelect a question: ')  

            if question_choice == 'question 1':
                self.run_question_1()
            elif question_choice == 'question 2':
                self.run_question_2()
            elif question_choice == 'question 3':
                self.run_question_3()
            elif question_choice == 'question 4':
                self.run_question_4()
            elif question_choice.lower() == 'quit':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option.")