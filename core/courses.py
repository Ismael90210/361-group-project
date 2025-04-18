class CourseManager:
    """
    Manages course creation and instructor assignment.
    """

    def __init__(self, course_id, course_code, title, semester, instructor_id):
        self.course_id = course_id
        self.title = title
        self.semester = semester
        self.instructor_id = instructor_id

    def create_course(self, course_data):
        """
        Creates a new course.

        Parameters:
            course_data (dict): Dictionary of course fields

        Preconditions: course_data must contain course fields, course does
        not already exist.

        Postconditions: course is created successfully.
        """
        pass

    def delete_course(self, course_id):
        """
        Parameters: course_id (int): The course ID of the course to be deleted.

        Preconditions: course must exist.

        Postconditions: the course is deleted successfully (everything set to none).
        """
        pass

        """
        Parameters: new_title (String): The new course title.
        
        Preconditions: new_title is a String, does not conflict with existing course title.
        
        Postconditions: course is updated successfully.
        """

    def update_id(self, new_id):
        pass

    """
            Parameters: new_title (int): The new course ID.

            Preconditions: new_id is an integer, does not conflict with existing course ID.

            Postconditions: course is updated successfully.
            """

    def update_title(self, new_title):
        pass

    """
            Parameters: new_semester (String): The new course semester.

            Preconditions: new_semester is a String, properly formatted as Fall/Spring, followed by a year.

            Postconditions: course is updated successfully.
            """

    def update_semester(self, new_semester):
        pass

    """
            Parameters: new_instructor (int): The new instructor's ID.

            Preconditions: new_instructor is an integer, does not conflict with existing instructor.

            Postconditions: course is updated successfully.
            """

    def update_instructor(self, new_instructor):
        pass


class Course:
    def __init__(self):
        self.course_id = None
        self.course_code = None
        self.title = None
        self.semester = None
        self.instructor_id = None

    # Add methods as needed
    pass


class LabSection:
    def __init__(self):
        self.lab_id = None
        self.section_number = None
        self.course_id = None
        self.assigned_ta_id = None

    # Add methods as needed
    pass


class Assignment:
    def __init__(self):
        self.assignment_id = None
        self.ta_id = None
        self.course_id = None
        self.type = None
        self.num_labs = None

    # Add methods as needed
    pass


class Notification:
    def __init__(self):
        self.notification_id = None
        self.sender_id = None
        self.recipient_id = None
        self.message = None
        self.timestamp = None

    # Add methods as needed
    pass

