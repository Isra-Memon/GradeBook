from gradebook import GradeBook, Student


def test_class_average_rounding_boundary(rounding_gradebook):
    # True average of averages = (79.99 + 80.0) / 2 = 79.995
    # Correct rounding to 2 decimals should give 80.0
    assert rounding_gradebook.class_average() == 80.0
