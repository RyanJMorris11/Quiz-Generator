import pymysql

class Database:

	def __init__(self):
		self.conn = pymysql.connect(host='localhost', user='root', passwd='theBois', db='Question_Database')
		self.cur = self.conn.cursor()

	
	def insertQuestion(self, question, answer, keyword):
		insert = """INSERT INTO Test_Questions (Question, Answer, Keyword) VALUES (%s, %s, %s)"""
		
		try:
			self.cur.execute(insert, (question, answer, keyword))
		except:
			print("cannot insert")
		self.conn.commit()
		
	def closeConnection(self):
		self.conn.close()
		