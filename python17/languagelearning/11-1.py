#单元测试和测试用例
import unittest
from name_funcation11 import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""方法名必须有test 开头"""
	def test_first_name(self):

		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name,'Janis Joplin')
		"""添加新测试"""
	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

unittest.main()
