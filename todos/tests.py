from django.test import TestCase
from .models import Todo

# Create your tests here.


class TodoTestCase(TestCase):
    def setUp(self):
        Todo.objects.create(title='first todo',
                            body='a body here', completed=True)

    def test_todo_title(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = 'first todo'
        self.assertEqual(todo.title, expected_object_name)

    def test_todo_body(self):
        todo = Todo.objects.get(id=1)
        expected_object_body = 'a body here'
        self.assertEqual(todo.body, expected_object_body)

    def test_todo_completion(self):
        todo = Todo.objects.get(id=1)
        expected_object_completion = True
        self.assertEqual(todo.completed, expected_object_completion)
