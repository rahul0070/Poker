import unittest

class pokerGame:
	def calculateHand(self):
		return 0
	
	def gameResult(self, player_one, player_two):
		return 0


def getWinner(player_one, player_two):
	game = pokerGame()
	result = game.gameResult(player_one, player_two)
	return 0

class OutcomesTest(unittest.TestCase):
	def test1(self):
		hand1 = [1,2,3]
		hand2 = [3,4,5]
		self.assertEqual(getWinner(hand1, hand2), 0)

if __name__ == '__main__':
    unittest.main()
