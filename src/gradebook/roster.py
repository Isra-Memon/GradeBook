class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if not (1 <= len(student.scores) <= 6):
            raise ValueError(
                f"Student must have between 1 and 6 scores, got {len(student.scores)}"
            )
        self.students.append(student)
