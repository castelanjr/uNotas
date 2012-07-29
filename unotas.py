# -*- coding: utf-8 -*-

from scraper import Scraper

import optparse

def main():
	p = optparse.OptionParser()
	p.add_option('--username', '-u')	
	p.add_option('--password', '-p')
	options, arguments = p.parse_args()
	if options.username and options.password:
		scraper = Scraper(options.username, options.password.decode('utf-8'))
		try:
			student = scraper.scrap()
			print '%s - %s' % (student.name, student.course)
			for semester in student.semesters:
				print '\nSemester: %s' % semester.period
				for discipline in semester.disciplines:
					print 'Discipline: %s' % discipline.name
					for grade in discipline.grades:
						print '%s - %s' % (grade.name, grade.value)
		except Exception, e:
			print 'Could not fetch grades: %s' % e.message
	else:
		print 'You must provide the username and password from Auto Atendimento.'


if __name__ == '__main__':
	main()
