import unittest
import requests

endpoint = 'http://findthebug.herokuapp.com/reversewords'

strings_to_reverse = {"string with all capital letter ": "ABCD", "string with two letters ": "is", "string with three letter" : "the",
					  "with numbers ": "1235", "with special characters" : "abcd@123!!!___", "with space in between ": "xyz abcde"}

class ReverseStringTest(unittest.TestCase):
	"""docstring for ReverseStringTest"""

	def testReverseSentence(self):
		payload = {}
		for case, eachStr in strings_to_reverse.items():
			payload['string'] = eachStr
			response = requests.get(endpoint, params=payload)
			reversedString = response.json()
			afterReverse = str(' '.join(w[::-1] for w in eachStr.split()))
			if reversedString == afterReverse:
				print("Actual: "+ reversedString, "Expected :"+ afterReverse,"   "+ case+": passed" )
				self.assertTrue(True)
			else:
				print("Actual: "+ reversedString, "Expected :"+ afterReverse,"   "+ case +": failed")
				self.assertFalse(False)


if __name__ == '__main__':
	unittest.main()
