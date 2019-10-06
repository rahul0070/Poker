import unittest

class pokerGame:
	# [A, K, Q, 10, 9, 8, 6, 5, 4, 3, 2]
	# [S, H, D, C]
	valueOfRank = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}

	def splitSuit(self, hand):
		suitList = []
		for i in hand:
			rl = i.split('-')
			suit = rl[0]
			suitList.append(suit)

		return suitList


	def splitRank(self, hand):
		rankList = []
		for i in hand:
			rl = i.split('-')
			rank = rl[1]
			rankList.append(self.valueOfRank.get(rank))

		return rankList

	def ifinList(self, element, listtoCheck):
		flag = 0
		for i in listtoCheck:
			if i[0] == element:
				flag = 1
		if flag == 1:
			return 1
		else:
			return 0


	def findPairs(self, hand):
		outList = []
		li = self.splitRank(hand)
		print(li)
		for i in range(len(li)):
			pairs = 0
			for j in range(len(li)):
				if li[j] == li[i]:
					pairs = pairs + 1

			if self.ifinList(li[i], outList) == 0:
				outList.append([li[i], pairs])
		return (outList)


	def check_fourOfKind(self, hand):
		flag = 0
		resultList = self.findPairs(hand)
		for i in resultList:
			if i[1] == 4:
				flag = 1

		if flag == 1:
			return 1
		else:
			return 0


	def check_StraightFlush(self, hand):
		rankl = self.splitRank(hand)
		flag = 0
		temp = rankl[0]
		for i in range(len(rankl)):
			if i != 0:
				if rankl[i] == temp-1:
					temp = rankl[i]
				else:
					if rankl[i] != 13:
						flag = 1

		if flag == 0:
			return 1
		else:
			return 0


	def check_FullSuit(self, hand):
		suitList = self.splitSuit(hand)
		flag = 0
		temp = suitList[0]
		for i in suitList:
			if i != temp:
				flag = 1
			temp = i

		if flag == 0:
			return 1
		else:
			return 0


	#Returns highest of any hand
	def returnHighest(self, hand):
		rankList = self.splitRank(hand)
		print(rankList)
		return max(rankList)


	def findWinner(self, score1, score2):
		if score1>score2:
			return 2
		elif score2>score1:
			return 1
		else:
			return 0


	def findHighest(self, hand1, hand2, combination):
		if combination == 10:
			value1 = self.returnHighest(hand1)
			value2 = self.returnHighest(hand2)

			if value1>value2:
				return 1
			elif value2>value1:
				return 2
			else:
				return 0

		elif combination == 1:
			h1 = self.splitRank(hand1)
			h2 = self.splitRank(hand2)

			if h1[0]>h2[0]:
				return 1
			elif h2[0]>h1[0]:
				return 2
			else:
				return 0


	def findCombination(self, hand):
		if self.check_FullSuit(hand) == 1:
			if self.check_StraightFlush(hand) == 1:
				return 1
	
		elif self.check_fourOfKind(hand) == 1:
			return 2

		elif self.check_StraightFlush(hand) == 1:
			return 5

		#highestCard = findHighest(hand)
		return 10
	

	def gameResult(self, player_one, player_two):
		scoreOfPlayer1 = self.findCombination(player_one)
		scoreOfPlayer2 = self.findCombination(player_two)
		print(scoreOfPlayer1, scoreOfPlayer2)

		if scoreOfPlayer1 == scoreOfPlayer2:
			result = self.findHighest(player_one, player_two, scoreOfPlayer1)

		else:
			result = self.findWinner(scoreOfPlayer1, scoreOfPlayer2)

		return result


def getWinner(player_one, player_two):
	game = pokerGame()
	gameResult = game.gameResult(player_one, player_two)
	print(gameResult)
	return gameResult


# class OutcomesTest(unittest.TestCase):
# 	def equalHands(self):
# 		hand1 = ['S6', 'C2', 'D9', 'D4', 'HK']
# 		hand2 = ['SJ', 'C2', 'D3', 'D6', 'H10']
# 		self.assertEqual(getWinner(hand1, hand2), 2)


# if __name__ == '__main__':
#     unittest.main()

#getWinner(['S-6', 'C-2', 'D-9', 'D-4', 'H-K'], ['S-A', 'C-2', 'D-3', 'D-6', 'H-10'])
#getWinner(['S-A', 'S-K', 'S-Q', 'S-J', 'S-10'], ['S-A', 'C-2', 'D-3', 'D-6', 'H-10'])
#getWinner(['S-A', 'S-K', 'S-Q', 'S-J', 'S-10'], ['S-5', 'S-4', 'S-3', 'S-2', 'S-A'])
getWinner(['S-A', 'C-A', 'D-A', 'C-A', 'S-10'], ['S-5', 'S-4', 'S-3', 'S-2', 'S-A'])
