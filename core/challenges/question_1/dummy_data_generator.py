import random
from faker import Faker


class DummyDataGenerator:
    """
    Class for generating dummy student and application data.

    Attributes:
        num_students (int): Number of students to generate.

    Methods:
        __init__(num_students): Initializes the DummyDataGenerator object.
        generate_students(): Generates dummy student data with unique IDs, names, and addresses.
        generate_applications(students): Generates dummy application data for the given list of students.
    """
    
    def __init__(self, num_students):
        """
        Initializes the DummyDataGenerator object with the specified parameters.

        Args:
            num_students (int): Number of students to generate.
        """
        self.fake = Faker()
        self.num_students = num_students


    def generate_students(self):
        """
        Generates dummy student data.

        Returns:
            list: A list of tuples containing (student_id, student_name, student_address).
        """
        students = []
        for student_id in range(1, self.num_students + 1):
            student_name = self.fake.name()
            student_address = self.fake.address()
            students.append((student_id, student_name, student_address))
        return students


    def generate_applications(self, students):
        """
        Generates dummy application data for the given list of students.

        Args:
            students (list): List of tuples containing (student_id, student_name, student_address).

        Returns:
            list: A list of tuples containing (application_id, student_id, score).
        """
        applications = []
        at_least_one_zero_application = False  # Flag to track if at least one student has 0 applications

        for student_id, _, _ in students:
            num_applications = random.randint(0, 5)  # Random number of applications (between 0 and 5)

            if num_applications == 0 and not at_least_one_zero_application:
                at_least_one_zero_application = True  # Set the flag to True for the first student with 0 applications
                break

            for _ in range(num_applications):
                application_id = len(applications) + 1
                score = random.randint(1, 100)  # Random score between 1 and 100
                applications.append((application_id, student_id, score))

        # If no student had 0 applications, add an application with 0 applications for a random student
        if not at_least_one_zero_application and students:
            student_id = random.choice(students)[0]

            # Remove all tuples with the selected student_id from applications list
            applications = [app for app in applications if app[1] != student_id]

        return applications

# Example usage
if __name__ == "__main__":
    num_students = 5  # Number of students

    # Create an instance of DummyDataGenerator
    data_generator = DummyDataGenerator(num_students)

    # Generate dummy student data
    students = data_generator.generate_students()

    # Generate dummy application data
    applications = data_generator.generate_applications(students)

    # Print generated student data
    print("Generated Student Data:")
    for student in students:
        print(student)

    # Print generated application data
    print("\nGenerated Application Data:")
    for application in applications:
        print(application)
