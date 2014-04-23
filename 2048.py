#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: 2048.py

import GameState

class GameClient:

	"""GameClient Class"""

	def __init__(self, n):
		self.length = n
		self.board = [0 for i in range(n * n)]
		self.num_of_empty = n * n
		#######
		self.max_value = 0
		self.tot_score = 0
	
	def getvalue(self, x, y):
		if x < 0 or y < 0 or x >= self.length or y >= self.length:
			return -1
		index = x * self.length + y
		return self.board[index]

	def setvalue(self, x, y, value):
		if x < 0 or y < 0 or x >= self.length or y >= self.length:
			return False
		index = x * self.length + y
		self.board[index] = value


def init_game(n):
	gc = GameClient(n)

def play(n, target):
	init_game(n)

if __name__ == '__main__':
	state = play(4, 32)
	if state == GameState.WIN:
		print 'You win!'
	else:
		print 'You lost!'
