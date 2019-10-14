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

	def test6(self):
		hand1 = ['S-A', 'C-A', 'D-6', 'C-A', 'S-A']  #Four of a kind
		hand2 = ['S-A', 'D-A', 'C-A', 'K-A', 'S-10']  #Four of a kind
		self.assertEqual(getWinner(hand1, hand2), 2)

	def test7(self):
		hand1 = ['S-A', 'C-A', 'D-A', 'C-3', 'S-3']  #Full House
		hand2 = ['S-A', 'S-A', 'S-A', 'D-5', 'S-5']  #Full House
		self.assertEqual(getWinner(hand1, hand2), 2)

	def test8(self):
		hand1 = ['S-3', 'C-A', 'D-7', 'C-7', 'S-A']  #Two Pair
		hand2 = ['S-A', 'S-5', 'S-6', 'D-6', 'S-A']  #Two Pair
		self.assertEqual(getWinner(hand1, hand2), 1)

	def test9(self):
		hand1 = ['S-9', 'C-9', 'D-5', 'C-7', 'S-3']  #Pair
		hand2 = ['S-9', 'D-9', 'S-6', 'D-10', 'S-5']  #Pair
		self.assertEqual(getWinner(hand1, hand2), 2)

	def test10(self):
		hand1 = ['S-10', 'C-7', 'D-5', 'C-3', 'S-K']  #Two Pair
		hand2 = ['S-10', 'S-7', 'S-5', 'D-2', 'S-K']  #Pair
		self.assertEqual(getWinner(hand1, hand2), 1)


if __name__ == '__main__':
    unittest.main()
