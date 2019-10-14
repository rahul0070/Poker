import unittest

class PokerGame:
	# [A, K, Q, 10, 9, 8, 6, 5, 4, 3, 2]
	valueOfRank = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, '10':9, 'J':10, 'Q':11, 'K':12, 'A':13}
	allScores = {'1':'Straight Flush', '4':'Flush', '2':'Four of a Kind', '3':'Full House', '5':'Straight', '6':'Three of a Kind', '7':'Two Pairs', '8':'Pair', '10':'Nothing'}

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

	def compare(self, first, second):
		if first>second:
			return 1
		elif second>first:
			return 2
		else:
			return 0

	def checkFlag(self, flag):
		if flag == 1:
			return 0
		elif flag == 0:
			return 1

	def ifinList(self, element, listtoCheck):
		flag = 1
		for i in listtoCheck:
			if i[0] == element:
				flag = 0
		
		return self.checkFlag(flag)


	def ifPresent(self, li, element):
		flag = 1
		for i in li:
			if i == element:
				flag = 0

		return self.checkFlag(flag)


	def removeAll(self, li, element):
		while self.ifPresent(li, element) == 1:
			li.remove(element)
		return li


	def find_KeyWithValue(self, element):
		for score, pattern in self.allScores.items():
			if pattern == element:
				return int(score)


	def findPairs(self, hand):
		outList = []
		li = hand
		for i in range(len(li)):
			pairs = 0
			for j in range(len(li)):
				if li[j] == li[i]:
					pairs = pairs + 1

			if self.ifinList(li[i], outList) == 0:
				outList.append([li[i], pairs])
		return outList


	def highestFrequentElement(self, li):
	 	pairs_list = self.findPairs(li)

	 	temp = 0
	 	for i in pairs_list:
	 		if i[1] > temp:
	 			temp = i[1]

	 	temp_list = []
	 	for i in pairs_list:
	 		if i[1] == temp:
	 			temp_list.append([i[0],i[1]])

	 	highestElement = 0
	 	for i in temp_list:
	 		if i[0]>highestElement:
	 			highestElement = i[0]
	 			Frequency = i[1]

	 	return (highestElement, Frequency)


	def compare_MaxFrequent(self, hand1, hand2):
		l1 = self.splitRank(hand1)
		l2 = self.splitRank(hand2)

		while len(l1)>0:
			h1 = self.highestFrequentElement(l1)
			h2 = self.highestFrequentElement(l2)

			if h1[0] == h2[0]:
				l1 = self.removeAll(l1, h1[0])
				l2 = self.removeAll(l2, h2[0])
				if len(l1) == 1:
					return self.compare(l1[0],l2[0])

			else:
				return self.compare(h1[0], h2[0])


	def check_StraightFlush(self, hand):
		rankl = self.splitRank(hand)
		rankl.sort(reverse = True)
		flag = 0
		temp = rankl[0]
		for i in range(len(rankl)):
			if i != 0:
				if rankl[i] != temp-1:
					if rankl[i] == 4 and temp == 13:
						temp = rankl[i]
					else:
						flag = 1

				else:
					temp = rankl[i]

		return self.checkFlag(flag)


	def check_FullSuit(self, hand):
		suitList = self.splitSuit(hand)
		flag = 0
		temp = suitList[0]
		for i in suitList:
			if i != temp:
				flag = 1
			temp = i

		return self.checkFlag(flag)


	def check_Combinations(self, hand):
		resultList = self.findPairs(self.splitRank(hand))

		if self.check_FullSuit(hand) == 1:
			if self.check_StraightFlush(hand) == 1:
				return 'Straight Flush'
			else:
				return 'Straight'

		for i in resultList:
			if i[1] == 4:
				return 'Four of a Kind'
			elif i[1] == 3:
				if len(resultList) == 2:
					return 'Full House'
				else:
					return 'Three of a Kind'
			elif i[1] == 2: 
				if len(resultList) == 3:
					return 'Two Pairs'
				else:
					return 'Pair'

		return 'Nothing'


	def findCombination(self, hand1, hand2):
		combinationOf_1 = self.find_KeyWithValue(self.check_Combinations(hand1))
		combinationOf_2 = self.find_KeyWithValue(self.check_Combinations(hand2))

		return combinationOf_1, combinationOf_2
	

	def gameResult(self, player_one, player_two):
		scoreOfPlayer1, scoreOfPlayer2 = self.findCombination(player_one, player_two)

		print('\nPlayer 1: ',self.allScores.get(str(scoreOfPlayer1)), ', Player 2: ',self.allScores.get(str(scoreOfPlayer2)))

		if scoreOfPlayer1 == scoreOfPlayer2:
			result = self.compare_MaxFrequent(player_one, player_two)
		else:
			result = self.compare(scoreOfPlayer2, scoreOfPlayer1)

		return result
