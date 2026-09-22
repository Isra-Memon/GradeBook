from .exceptions import GradeBookIOError


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.roll_no == student.roll_no:
                raise ValueError(f"Roll number {student.roll_no} already exists")
        self.students.append(student)

    def find_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None

    def class_average(self):
        total = sum(s.average() for s in self.students if s.scores)
        count = len([s for s in self.students if s.scores])
        return round(total / count, 2) if count else 0

    def save_to_file(self, path):
        lines = [f"{s.name},{s.roll_no},{s.average()}" for s in self.students]
        content = "\n".join(lines)
        try:
            with open(path, "w") as f:
                f.write(content)
        except OSError as e:
            raise GradeBookIOError(f"Could not save gradebook to {path}: {e}")
