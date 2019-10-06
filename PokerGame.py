import unittest

class pokerGame:
	# [A, K, Q, 10, 9, 8, 6, 5, 4, 3, 2]
	# [S, H, D, C]
	def findWinner(self, score1, score2):


	def findHighest(self, hand1, hand2):
		value = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':6, '10':7, 'Q':8, 'K':9, 'A':10}


	def findSpecial(self, hand):
		highestCard = findHighest(hand)
		return 0
	
	def gameResult(self, player_one, player_two):
		scoreOfPlayer1 = findSpecial(player_one)
		scoreOfPlayer2 = findSpecial(player_two)
		
		if scoreOfPlayer1 == 0 and scoreOfPlayer2 == 0:
			result = findHighest(player_one, player_two)
		else:
			result = findWinner(scoreOfPlayer1, scoreOfPlayer2)


def getWinner(player_one, player_two):
	game = pokerGame()
	result = game.gameResult(player_one, player_two)
	return 0

class OutcomesTest(unittest.TestCase):
	def equalHands(self):
		hand1 = [S6, C2, D9, D4, HK]
		hand2 = [SA, C2, D3, D6, H10]
		self.assertEqual(getWinner(hand1, hand2), 2)

if __name__ == '__main__':
    unittest.main()
