from gradebook import GradeBook, Student


def test_class_average_rounding_boundary():
    gb = GradeBook()

    s1 = Student("Student A", 1)
    s1.add_score(79.99)
    gb.add_student(s1)

    s2 = Student("Student B", 2)
    s2.add_score(80.0)
    gb.add_student(s2)

    # True average of averages = (79.99 + 80.0) / 2 = 79.995
    # Correct rounding to 2 decimals should give 80.0
    assert gb.class_average() == 80.0
