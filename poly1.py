#! /usr/bin/python

### PolyMorphisam####Method over riding
#*************************#

import os

class A:
	def __init__(self):
		self.enumber =111
		self.ename = 'computer'
		self.ecity='hyd'
		self.edsgn='manager'

	def output(self):
		print self.enumber,self.ename


class B(A): # Calss B inherits from Class A
	def output(self):
		print self.ecity,self.edsgn


obj=B()
#Child Method over rides the method
obj.output()
