from gradebook import GradeBook, Student


def test_class_average_rounding_boundary(rounding_gradebook):
    # True average of averages = (79.99 + 80.0) / 2 = 79.995
    # Correct rounding to 2 decimals should give 80.0
    assert rounding_gradebook.class_average() == 80.0

def test_class_average_empty_gradebook(empty_gradebook):
    assert empty_gradebook.class_average() == 0


def test_class_average_single_student(empty_gradebook):
    s1 = Student("Solo Student", 1)
    s1.add_score(88)
    empty_gradebook.add_student(s1)

    assert empty_gradebook.class_average() == 88.0
