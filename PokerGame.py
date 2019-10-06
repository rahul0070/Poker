import unittest

class PokerGame:
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

	def compare(self, first, second):
		if first>second:
			return 1
		elif second>first:
			return 2
		else:
			return 0

	def ifinList(self, element, listtoCheck):
		flag = 0
		for i in listtoCheck:
			if i[0] == element:
				flag = 1
		if flag == 1:
			return 1
		else:
			return 0

	def findMaxValue(self, list1, list2, n):
		for i in list1:
			if i[1] == n:
				val1 = i[0]
		for i in list2:
			if i[1] == n:
				val2 = i[0]

		return val1, val2


	def findPairs(self, hand):
		outList = []
		li = self.splitRank(hand)
		for i in range(len(li)):
			pairs = 0
			for j in range(len(li)):
				if li[j] == li[i]:
					pairs = pairs + 1

			if self.ifinList(li[i], outList) == 0:
				outList.append([li[i], pairs])
		return outList


	def findPairs2(self, hand):
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


	def find_maximumPair(self, listOfValues):
		li = []
		li2 = []
		for i in listOfValues:
			li.append(i[1])

		return max(li)


	def compare_HighestNotEqual(self, list1, list2):
		i = 0
		while len(list1)>0:
			if list1[i] == list2[i]:
				list1.remove(list1[i])
				list2.remove(list2[i])
			else:
				return self.compare(list1[i], list2[i])


	def compare_SinglePair(self, hand1, hand2):
		h1_list = []
		h2_list = []

		for i in hand1:
			if i[1] == 1:
				h1_list.append(i[0])

		for i in hand2:
			if i[1] == 1:
				h2_list.append(i[0])

		h1_list.sort(reverse = True)
		h2_list.sort(reverse = True)
		return self.compare_HighestNotEqual(h1_list, h2_list)


	def compareHands(self, hand1, hand2):
		h1 = self.findPairs(hand1)
		h2 = self.findPairs(hand2)

		maxVal = self.find_maximumPair(h1)

		if maxVal == 4:
			val1, val2 = self.findMaxValue(h1, h2, 1)

		elif maxVal == 3:
			val1, val2 = self.findMaxValue(h1, h2, 2)

		elif maxVal == 2:
			val_pair_1 = []
			val_pair_2 = []
			for i in h1:
				if i[1] == 2:
					val_pair_1.append(i[0])
			val_pair_1.sort()

			for i in h2:
				if i[1] == 2:
					val_pair_2.append(i[0])
			val_pair_2.sort()

			if len(val_pair_1) > 1:
				if max(val_pair_1) != max(val_pair_2):
					val1 = max(val_pair_1)
					val2 = max(val_pair_2)

				elif val_pair_1[len(val_pair_1)-2] != val_pair_2[len(val_pair_2)-2]:
					val1 = val_pair_1[len(val_pair_1)-2]
					val2 = val_pair_2[len(val_pair_2)-2]

				else:
					val_result = self.compare_SinglePair(h1, h2)
					return val_result

			elif len(val_pair_1) == 1:
				if val_pair_1[0] == val_pair_2[0]:
					val_result = self.compare_SinglePair(h1, h2)
					return val_result

				else:
					return compare(val_pair_1[0], val_pair_2[0])
		return self.compare(val1, val2)


	def check_Pairs(self, hand):
		flag = ''
		resultList = self.findPairs(hand)
		for i in resultList:
			if i[1] == 4:
				return 'fourOfaKind'
			elif i[1] == 3:
				if len(resultList) == 2:
					return 'fullHouse'
				else:
					return 'threeOfaKind'
			elif i[1] == 2: 
				if len(resultList) == 3:
					return 'twoPairs'
				else:
					return 'Pair'
		return flag


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

			return self.compare(h1[0], h2[0])

		elif combination == 2:
			result = self.compareHands(hand1, hand2)
			return result

		elif combination == 3:
			result = self.compareHands(hand1, hand2)
			return result

		elif combination == 7:
			result = self.compareHands(hand1, hand2)
			return result

		elif combination == 8:
			result = self.compareHands(hand1, hand2)
			return result


	def findCombination(self, hand):
		if self.check_FullSuit(hand) == 1:
			if self.check_StraightFlush(hand) == 1:
				return 1
			else:
				return 4
	
		if self.check_Pairs(hand) == 'fourOfaKind':
			return 2

		elif self.check_Pairs(hand) == 'fullHouse':
			return 3

		elif self.check_StraightFlush(hand) == 1:
			return 5

		elif self.check_Pairs(hand) == 'threeOfaKind':
			return 6

		elif self.check_Pairs(hand) == 'twoPairs':
			return 7

		elif self.check_Pairs(hand) == 'Pair':
			return 8

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
