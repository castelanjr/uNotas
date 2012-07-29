# -*- coding: utf-8 -*-

import urllib2, urllib

from models import Student, Semester, Discipline, Grade

from BeautifulSoup import BeautifulSoup

class Scraper(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password.encode('latin-1')
		
	def scrap(self):
		cookie = urllib2.HTTPCookieProcessor()
		opener = urllib2.build_opener(cookie)
		urllib2.install_opener(opener)

		data = {}
		data['i_Login'] = self.username
		data['i_Senha'] = self.password
		data = urllib.urlencode(data)

		url = 'https://memphis.ulbranet.com.br/pls/ulbra24/AAWEB.login'
		url2 = 'https://memphis.ulbranet.com.br/aa/notas'

		opener.open(url, data)
		
		request = urllib2.Request(url2)
		response = urllib2.urlopen(request)
		soup = BeautifulSoup(response.read())

		student = Student()
		student.course = soup.find("a", "active").contents[0].strip()
		student.name = soup.find("div", {"id": "cabprint_inf"}).contents[4].strip()

		for grade in soup.findAll("li", {"id": "li_notas"}):
			semester_obj = Semester(grade.find("a", "link").contents[0])
			for discipline in grade.findAll("div", "notas-bloco"):
				i = 0
				for total in discipline.findAll("div", "notas-texto"):
					value = total.parent.findAll("div", "notas-final")[i].contents[0].strip()
					value = value.replace("\n", "").replace("\t", "")
					grade_total_obj = Grade("Total", value)
	
					discipline_obj = Discipline(total.find("div", "notas-disciplina").contents[0].strip())
					
					for partial in total.findAll("div", "notas-parciais"):
						grade_value = partial.b.contents[0].string.replace("\n", "").replace("\t", "").strip()
						grade_name = partial.contents[0].string.replace("\n", "").replace("\t", "").strip()
						grade_disc = Grade(str(grade_name), str(grade_value))
						discipline_obj.grades.append(grade_disc)
					discipline_obj.grades.append(grade_total_obj)
					i += 1
					semester_obj.disciplines.append(discipline_obj)
			student.semesters.append(semester_obj)
					

		return student
