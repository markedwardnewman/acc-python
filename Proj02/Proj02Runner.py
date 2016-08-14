import turtle

class Runner:
    """class used to instantiate immutable code for assignments """

    student_name = "Mark Newman"

    def __init__(self, new_value):
        """ Add an unspecified value to Runner """

        self.value = new_value

    
    def run(self):
        """ returns a tuple that contains a value (color), a turtle object (with overidden penshape and size) and the student's name  """

        aTurtle = turtle.Turtle()
        aTurtle.shape("turtle")
        aTurtle.pensize(5)

        aTuple = (self.value, aTurtle, self.student_name)

        return aTuple
