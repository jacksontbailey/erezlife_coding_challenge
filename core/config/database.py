import os
import psycopg2
from core.challenges.question_1.dummy_data_generator import DummyDataGenerator
from dotenv import load_dotenv, find_dotenv

class DatabaseConfig:
    """
    Class representing the configuration settings for PostgreSQL database connection and table creation.

    Attributes:
        db_params (dict): Dictionary containing database connection parameters including dbname, user, password, host, and port.
        dotenv_file (str): Path to the .env file containing environment variables for database configuration.
        
    Methods:
        __init__(dotenv_file): Initializes the DatabaseConfig object with the path to the .env file.
        _get_env_variable(variable_name): Private method to retrieve environment variables from the .env file.
        create_tables(): Creates 'student' and 'application' tables in the specified PostgreSQL database.
        add_dummy_data(num_students=5, num_applications_per_student=3): 
            Adds dummy student and application data to the database.

    """


    def __init__(self):
        """
        Initializes the DatabaseConfig object with the path to the .env file containing database configuration.

        Args:
            dotenv_file (str): Path to the .env file.
        """
        self.dotenv_file = find_dotenv()

        # load environment variables from .env file
        load_dotenv(self.dotenv_file)

        self.db_params = {
            'dbname': self._get_env_variable("database_name"),
            'user': self._get_env_variable("database_user"),
            'password': self._get_env_variable("database_pass"),
            'host': self._get_env_variable("database_host"),
            'port': self._get_env_variable("database_port")
        }


    def _get_env_variable(self, variable_name):
        """
        Private method to retrieve environment variables from the .env file.

        Args:
            variable_name (str): Name of the environment variable.

        Returns:
            str: Value of the environment variable.
        """
        return os.getenv(variable_name)


    def create_tables(self):
        """
        Creates 'student' and 'application' tables in the specified PostgreSQL database.

        Raises:
            psycopg2.Error: If an error occurs while creating the tables.
        """
        # Establish a connection to the database
        try:
            with psycopg2.connect(**self.db_params) as connection:
                with connection.cursor() as cursor:
                    # Create the student table
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS student (
                            id SERIAL PRIMARY KEY,
                            name TEXT,
                            address TEXT
                        );
                    ''')

                    # Create the application table with foreign key constraint
                    cursor.execute('''
                        CREATE TABLE IF NOT EXISTS application (
                            id SERIAL PRIMARY KEY,
                            student_id INTEGER REFERENCES student(id),
                            score INTEGER
                        );
                    ''')

            print("Tables created successfully.")

        except psycopg2.Error as e:
            print("Error: Unable to create tables.")
            print(e)


    def add_dummy_data(self, num_students=5, num_applications_per_student=3):
        """
        Add dummy student and application data to the database.

        Args:
            num_students (int): Number of students to generate. Defaults to 5.
            num_applications_per_student (int): Number of applications to generate per student. Defaults to 3.
        """
        # Generate dummy data
        data_generator = DummyDataGenerator(num_students, num_applications_per_student)
        students = data_generator.generate_students()
        applications = data_generator.generate_applications(students)

        try:
            # Establish a connection to the database
            with psycopg2.connect(**self.db_params) as connection:
                with connection.cursor() as cursor:
                    # Insert student data into the student table
                    cursor.executemany(
                        'INSERT INTO student (id, name, address) VALUES (%s, %s, %s)',
                        students
                    )

                    # Insert application data into the application table
                    cursor.executemany(
                        'INSERT INTO application (id, student_id, score) VALUES (%s, %s, %s)',
                        applications
                    )

                    print(f"Added {num_students} students and their applications to the database.")

        except psycopg2.Error as e:
            print("Error: Unable to add dummy data to the database.")
            print(e)



DB_SETTING = DatabaseConfig()