import unittest
from main import app


class Test(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_sphere(self):
        with app.test_client() as client:
            data = {'shape': 'sphere', 'radius': '3', 'precision': '1'}
            response = self.app.post('/calculate_volume', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'113.1', response.data)

    def test_cube(self):
        with app.test_client() as client:
            data = {'shape': 'cube', 'side': '5', 'precision': '2'}
            response = self.app.post('/calculate_volume', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'125.0', response.data)

    def test_cylinder(self):
        with app.test_client() as client:
            data = {'shape': 'cylinder','height': '1', 'radius': '1', 'precision': '1'}
            response = self.app.post('/calculate_volume', data=data)
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'3.1', response.data)

if __name__ == '__main__':
    unittest.main()