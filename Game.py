from Poker import PokerGame
import unittest

def getWinner(player_one, player_two):
	Game = PokerGame()
	return Game.gameResult(player_one, player_two)

class OutcomesTest(unittest.TestCase):
	def test1(self):
		hand1 = ['S-6', 'C-2', 'D-9', 'D-4', 'H-K']
		hand2 = ['S-A', 'C-2', 'D-3', 'D-6', 'H-10']
		self.assertEqual(getWinner(hand1, hand2), 2)

	def test2(self):
		hand1 = ['S-A', 'S-K', 'S-Q', 'S-J', 'S-10']
		hand2 = ['S-A', 'C-2', 'D-3', 'D-6', 'H-10']
		self.assertEqual(getWinner(hand1, hand2), 1)

	def test3(self):
		hand1 = ['S-A', 'S-K', 'S-Q', 'S-J', 'S-10'] #Straight flush
		hand2 = ['S-5', 'S-4', 'S-3', 'S-2', 'S-A']  #Straight flush
		self.assertEqual(getWinner(hand1, hand2), 1)

	def test4(self):
		hand1 = ['S-A', 'C-A', 'D-A', 'C-A', 'S-10'] #Four of a kind
		hand2 = ['S-5', 'S-4', 'S-3', 'S-2', 'S-A']  #Straight Flush
		self.assertEqual(getWinner(hand1, hand2), 2)

	def test5(self):
		hand1 = ['S-A', 'C-A', 'D-2', 'C-5', 'S-8']   #Two Pair
		hand2 = ['S-5', 'S-A', 'S-6', 'S-2', 'S-10']  #Flush
		self.assertEqual(getWinner(hand1, hand2), 2)


if __name__ == '__main__':
    unittest.main()
