import Tasks.Triangle_task


def test_01_unexisted_triangle_error():
    my_triangle = Tasks.Triangle_task.Triangle(3, 1, 6)
    assert my_triangle.is_exist is False


def test_02_unexisted_triangle_negative_value():
    my_triangle = Tasks.Triangle_task.Triangle(3, -3, 6)
    assert my_triangle.is_exist is False


def test_03_fullset_for_isosceles_triangle():
    my_triangle = Tasks.Triangle_task.isosceles_triangle
    assert my_triangle.triangle_perimeter == 21
    assert my_triangle.triangle_square == 21
    assert my_triangle.triangle_type == "Треугольник равнобедренный"


def test_04_fullset_for_equalsided_triangle():
    my_triangle = Tasks.Triangle_task.equalsided_triangle
    assert my_triangle.triangle_perimeter == 15
    assert my_triangle.triangle_square == 10
    assert my_triangle.triangle_type == "Треугольник равностронний"


def test_05_fullset_for_rightangled_triangle():
    my_triangle = Tasks.Triangle_task.rightangled_triangle
    assert my_triangle.triangle_perimeter == 18.8
    assert my_triangle.triangle_square == 15
    assert my_triangle.triangle_type == "Треугольник прямоугольный"


def test_06_fullset_for_random_triangle():
    my_triangle = Tasks.Triangle_task.random_triangle
    assert my_triangle.triangle_perimeter == 21
    assert my_triangle.triangle_square == 10
    assert my_triangle.triangle_type == "Треугольник разносторонний"