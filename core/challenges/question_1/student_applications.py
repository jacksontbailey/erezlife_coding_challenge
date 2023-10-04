import psycopg2
from core.config.database import DB_SETTING

def get_student_applications():
    """
    Retrieve student information along with the number of applications each student has.
    
    Returns:
        list: A list of tuples containing (student_id, student_name, num_applications).
    """
    try:
        # Create a DatabaseConfig instance
        db_config = DB_SETTING

        # Establish a connection to the database
        with psycopg2.connect(**db_config.db_params) as connection:
            with connection.cursor() as cursor:
                # SQL query to retrieve student information and number of applications
                query = """
                    SELECT s.id AS student_id, s.name AS student_name, COALESCE(COUNT(a.id), 0) AS num_applications
                    FROM student s
                    LEFT JOIN application a ON s.id = a.student_id
                    GROUP BY s.id, s.name
                    ORDER BY num_applications DESC, s.name;
                """

                # Execute the query
                cursor.execute(query)

                # Fetch all rows
                student_applications = cursor.fetchall()

        return student_applications

    except psycopg2.Error as e:
        print("Error: Unable to fetch student applications.")
        print(e)
        return []