import pymysql

class Database:

	def __init__(self):
		self.conn = pymysql.connect(host='localhost', user='root', passwd='theBois', db='Question_Database')
		self.cur = self.conn.cursor()

	
	def insertQuestion(self, question, answer, keyword):
		insert = """INSERT INTO Test_Questions (Question, Answer, Keyword) VALUES (%s, %s, %s)"""
		
		try:
			if (question != "" and answer != "" and question != "..." and answer != "..."):
				self.cur.execute(insert, (question, answer, keyword))
		except:
			print("cannot insert")
		self.conn.commit()
		
	def selectQuestions(self, keyword):
		select = """SELECT Question, Answer FROM Test_Questions WHERE Keyword=%s ORDER BY RAND() LIMIT 20;"""
		
		try:
			self.cur.execute(select, (keyword))
			result = self.cur.fetchall()
		except:
			print("cannot select")
			
		return result
		self.conn.commit()
		
	def closeConnection(self):
		self.conn.close()
		
	
		