import unittest
import requests

class TestServerUp(unittest.TestCase):
	def setUp(self):
		self.uri = 'http://localhost/'

	def test_index_is_up(self):
		r = requests.get(self.uri)
		self.assertEqual(r.status_code, '200')


if __name__ == '__main__':
	unittest.main()