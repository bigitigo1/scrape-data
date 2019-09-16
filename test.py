from urllib.request import urlopen
import mysql.connector
from bs4 import BeautifulSoup

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="test"
)
web = "https://vnexpress.net/giao-duc"
soup = BeautifulSoup(urlopen(web),"html.parser")
list_web = []
for link in soup.find_all('a'):
	if web in str(link.get('href')):
		list_web.append(link.get('href'))

list_web = list(set(list_web))

for link_education in list_web:
	sub_soup = BeautifulSoup(urlopen(link_education),"html.parser")

	mycursor = mydb.cursor()
	sql = "INSERT INTO education (tieude, noidung) VALUES (%s, %s)"
	val = (sub_soup.title.string, sub_soup.article.text)
	mycursor.execute(sql,val)
	mydb.commit()
mydb.close()