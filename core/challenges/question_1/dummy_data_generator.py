import random
from faker import Faker


class DummyDataGenerator:
    """
    Class for generating dummy student and application data.

    Attributes:
        num_students (int): Number of students to generate.
        num_applications_per_student (int): Number of applications to generate per student.

    Methods:
        __init__(num_students, num_applications_per_student): Initializes the DummyDataGenerator object.
        generate_students(): Generates dummy student data with unique IDs, names, and addresses.
        generate_applications(students): Generates dummy application data for the given list of students.
    """
    
    def __init__(self, num_students, num_applications_per_student):
        """
        Initializes the DummyDataGenerator object with the specified parameters.

        Args:
            num_students (int): Number of students to generate.
            num_applications_per_student (int): Number of applications to generate per student.
        """
        self.fake = Faker()
        self.num_students = num_students
        self.num_applications_per_student = num_applications_per_student


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
        for student_id, _, _ in students:
            for _ in range(self.num_applications_per_student):
                application_id = len(applications) + 1
                score = random.randint(1, 100)  # Random score between 1 and 100
                applications.append((application_id, student_id, score))
        return applications

# Example usage
if __name__ == "__main__":
    num_students = 5  # Number of students
    num_applications_per_student = 3  # Number of applications per student

    # Create an instance of DummyDataGenerator
    data_generator = DummyDataGenerator(num_students, num_applications_per_student)

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
