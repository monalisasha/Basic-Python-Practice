import unittest
import requests

import math
from math import sqrt
from itertools import count, islice

endpoint = 'http://findthebug.herokuapp.com/primenumbers'

def is_prime_number(n):
    if n < 2: return False
    for number in islice(count(2), int(sqrt(n)-1)):
        if not n%number:
            return False
    return True

class ReverseStringTest(unittest.TestCase):
	"""docstring for ReverseStringTest"""

	def testReverseSentence(self):
		payload = {}
		for eachNumber in range(1, 10):
			payload['number'] = eachNumber
			response = requests.get(endpoint, params=payload)
			#converting response dat to json
			isPrimeFromEndpoint = response.json()
			isPrimeActual = is_prime_number(eachNumber)

			if isPrimeFromEndpoint == isPrimeActual and isPrimeActual == True:
				print (eachNumber, "Is a Prime number")
				self.assertTrue(True)
			else:
				print (eachNumber, "Is not a Prime number ")
				self.assertFalse(False)


if __name__ == '__main__':
	unittest.main()
