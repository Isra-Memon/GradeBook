def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError(f"Invalid score: {score}. Must be between 0 and 100.")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.scores = []
    def add_score(self, score):
        self.scores.append(score)
    def average(self):
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
    def grade_letter(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


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
        # BUG 4: incorrect rounding (truncates instead of rounding properly)
        total = sum(s.average() for s in self.students if s.scores)
        count = len([s for s in self.students if s.scores])
        return int((total / count) * 100) / 100 if count else 0


if __name__ == "__main__":
    gb = GradeBook()
    isra = Student("Isra", 101)
    isra.add_score(85)
    isra.add_score(90)
    gb.add_student(isra)
    print("Isra's average:", isra.average())
    print("Isra's grade:", isra.grade_letter())
    print("Class average:", gb.class_average())
