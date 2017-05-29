#! /usr/bin/python
#-*- coding: utf-8 -*-
from types import *
class NAF:
	def __init__(self, d=0):
		self.value = []
		self.sign = 0
		self.__type__ = "NAF"
		if d != 0:
			if d < 0:
				self.sign = 1
				d = 0 - d
			while d > 0:
				if d & 1 == 1:
					d_i = 2-(d%4)
					d = d - d_i
				else:
					d_i = 0
				d /= 2
				self.value.append(d_i)
		else:
			self.value.append(0)

	def naf(self, d):
		self.value = []
		if d == 0:
			self.value = [0]
		elif d < 0:
			self.sign = 1
			d = 0 - d
		while d > 0:
			if d & 1 == 1:
				d_i = 2-(d%4)
				d = d - d_i
			else:
				d_i = 0
			d /= 2
			self.value.append(d_i)

	def hamming(self):
		return len(self.value) - self.value.count(0)

	def int(self):
		l = len(self.value)
		i = 0
		tmp = 0
		while i < l:
			tmp += self.value[i] * (2**i)
			i += 1
		if self.sign:
			tmp = 0 - tmp
		return tmp

	def __add__(self, a):
		if type(a) == IntType:
			return self.int() + a
		elif type(a) == InstanceType:
			if "__type__" in a.__dict__.keys():
				if a.__dict__["__type__"] == "NAF":
					return self.int() + a.int()
		else: 
			print "error of type"


	def __radd__(self, a):
		if type(a) == IntType:
			return self.int() + a
		elif type(a) == InstanceType:
			if "__type__" in a.__dict__.keys():
				if a.__dict__["__type__"] == "NAF":
					return self.int() + a.int()
		else: 
			print "error of type"

n = NAF(56759079395191398102086508490449101313077112642937421927033154997581275717634)
#print n.value