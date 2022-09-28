import pytest
from rest_framework.test import APIClient

from students.models import Student, Course
from model_bakery import baker


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=2, students=students)

    response = client.get(f'/api/v1/courses/{courses[0].id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == courses[0].name


@pytest.mark.django_db
def test_get_lis_course(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=5, students=students)

    response = client.get(f'/api/v1/courses/')
    data = response.json()

    assert len(courses) == len(data)
    for i, c in enumerate(data):
        assert c['id'] == courses[i].id


@pytest.mark.django_db
def test_filter_id(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=5, students=students)

    response = client.get(f'/api/v1/courses/?id={courses[1].id}')
    data = response.json()

    assert data[0]['id'] == courses[1].id


@pytest.mark.django_db
def test_filter_name(client, student_factory, course_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=5, students=students)

    response = client.get(f'/api/v1/courses/?name={courses[2].name}')
    data = response.json()

    assert data[0]['name'] == courses[2].name


@pytest.mark.django_db
def test_create_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'Math'})
    data = response.json()

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_patch_course(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=5, students=students)

    response = client.patch(f'/api/v1/courses/{courses[0].id}/', data={'name': 'Math'})
    data = response.json()

    assert data['name'] == 'Math'


@pytest.mark.django_db
def test_delete_course(client, course_factory, student_factory):
    students = student_factory(_quantity=5)
    courses = course_factory(_quantity=5, students=students)
    count = Course.objects.count()

    response = client.delete(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count -1