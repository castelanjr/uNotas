#-*- coding: utf-8 -*-

class Student(object):
	def __init__(self):
		self.name = ''
		self.course = ''
		self.semesters = []

class Semester(object):
	def __init__(self, period):
		self.period = period
		self.disciplines = []

class Discipline(object):
	def __init__(self, name):
		self.name = name
		self.grades = []

class grade(object):
	def __init__(self, name, value):
		self.name = name
		self.value = value
