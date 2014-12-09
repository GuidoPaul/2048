#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: 2048.py

import sys
import random
import GameState

class GameClient:

	def __init__(self, n):
		self.length = n
		self.board = [0 for i in range(n * n)]
		self.num_of_empty = n * n
		self.max_value = 2
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
	
	def __len__(self):
		return self.length

def set_random_number(gc, first):

	"""@todo: 在空格处放置随机值
	:first: 是否在为初始的两个数
	"""

	n = len(gc)
	while not gc.num_of_empty == 0:
		x = random.randint(0, n - 1)
		y = random.randint(0, n - 1)
		if gc.getvalue(x, y) == 0:
			key = random.random()
			if key <= 0.2:
				value = 4
			else:
				value = 2
			if first and gc.max_value < value:
				gc.max_value = value
			gc.setvalue(x, y, value)
			gc.num_of_empty -= 1
			return True
	return False

def init_game(n):

	gc = GameClient(n)
	set_random_number(gc, 1)
	return gc, GameState.NORMAL

def print_board(target, gc):

	"""@todo: 输出棋盘
	"""

	n = len(gc)
	line = '+----+----+----+----+'

	print target, 'max:', str(gc.max_value), 'score:', gc.tot_score
	print line
	for i in range(n):
		sys.stdout.write('|')
		for j in range(n):
			value = gc.getvalue(i, j)
			if(value == 0):
				value = ''
			sys.stdout.write(str(value).rjust(4) + '|')
		sys.stdout.write('\n')
		print line
	sys.stdout.flush()

def combinable(gc):

	'''@todo: 在棋盘放满的情况下, 检查是否还有可组合的数字
	'''

	n = len(gc)
	for i in range(n):
		for j in range(n):
			value = gc.getvalue(i, j)
			if value == 0:
				return True
			if value == gc.getvalue(i + 1, j):
				return True
			if value == gc.getvalue(i, j + 1):
				return True
	return False

def get_dir(gc):

	"""@todo: 获取键入的方向
	"""

	dir = raw_input("Enter a direction, like 'a'(Left), w'(Up), 'd'(Right), 's'(Down) :")
	if dir == 'a':
		return GameState.LEFT
	elif dir == 'w':
		return GameState.UP
	elif dir == 'd':
		return GameState.RIGHT
	elif dir == 's':
		return GameState.DOWN
	else:
		return None

def Swap(gc, dir):

	"""@todo: 移动
	:dir: 键入的方向
	"""

	def xset_cur(i, j, value):
		gc.setvalue(i, j, value)
	def yset_cur(i, j, value):
		gc.setvalue(j, i, value)
	def xget_cur(i, j):
		return gc.getvalue(i, j)
	def yget_cur(i, j):
		return gc.getvalue(j, i)

	col_indexs = range(len(gc))

	if dir == GameState.LEFT:
		get_cur = xget_cur
		set_cur = xset_cur
		delta = 1
	elif dir == GameState.UP:
		get_cur = yget_cur
		set_cur = yset_cur
		delta = 1
	elif dir == GameState.RIGHT:
		get_cur = xget_cur
		set_cur = xset_cur
		delta = -1
		col_indexs = col_indexs[::-1]
	elif dir == GameState.DOWN:
		get_cur = yget_cur
		set_cur = yset_cur
		delta = -1
		col_indexs = col_indexs[::-1]
	else:
		return 0, False

	score = 0
	moved = False
	for i in range(len(gc)):
		for j in col_indexs:
			if get_cur(i, j) == 0:
				continue
			'''符合条件的相同的数字组合'''
			k = j + delta
			while get_cur(i, k) == 0:
				k += delta
			if get_cur(i, j) == get_cur(i, k):
				set_cur(i, j, get_cur(i, j) * 2)
				set_cur(i, k, 0)
				if get_cur(i, j) > gc.max_value:
					gc.max_value = get_cur(i, j)
				score += get_cur(i, j)
				gc.num_of_empty += 1
				moved = True

			'''略过中间空余的格子'''
			k = j
			while get_cur(i, k - delta) == 0:
				k -= delta
			if not k == j:
				set_cur(i, k, get_cur(i, j))
				set_cur(i, j, 0)
				moved = True
	
	gc.tot_score += score
	return moved

def play(n, target, debug = False):

	"""@todo: 主方法
	:n: 棋盘边长
	:target: 目标分数
	"""
	gc, state = init_game(n)
	set_random_number(gc, 1)

	if debug:
		print_board(target, gc)
		
		while state == GameState.NORMAL:
			if gc.max_value >= target:
				state = GameState.WIN
				break
			elif gc.num_of_empty == 0 and not combinable(gc):
				state = GameState.LOST
				break

			dir = get_dir(gc)
			moved = Swap(gc, dir)
			if dir != None:
				set_random_number(gc, 0)
			# if moved and debug:
			if debug:
				print_board(target, gc)
	return state

if __name__ == '__main__':
	state = play(4, 2048, debug = True)
	if state == GameState.WIN:
		print 'You win!'
	else:
		print 'You lost!'
