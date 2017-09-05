#! /usr/bin/env python
# -*- coding: utf-8 -*-

class VPlayer(object):
	"""
	Video Player
	"""
	def __init__(self):
		super(VPlayer, self).__init__()
		# init play property to False
		self._play = False

	@property
	def elapsed(self):
		"""
		Time ......
		"""
		return self._elapsed

	@property
	def play(self):
		"""
		play
		True make it play
		False make it stop
		"""
		return self._play
	@play.setter
	def play(self, play):
		self._play = play
