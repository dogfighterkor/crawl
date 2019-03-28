from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import datetime
from dateutil.parser import parse
import sys
from crawler.db import save

def parsing(html):
	soup = BeautifulSoup(html, "html.parser")
	list = soup.find_all("div", {"class" : "desc_boxthumb"})
	for li in list:
		name = li.find("strong", {"class" : "tit_join"})
		point = li.find("em", {"class" : "emph_grade"})
		releasedatedl = li.find("dl", {"class" : "list_state"})
		releasedate = releasedatedl.find("dd").text
		releasedate = releasedate[:10].strip()
		rdate = parse(releasedate)
		save(name.text.strip(), rdate, point.text.strip(), "DAUM")
def DAUM():
	driver = webdriver.PhantomJS('/home/ec2-user/temp2/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
	list = ['https://movie.daum.net/premovie/released?opt=reserve&page=1']
	for site in list:
		driver.get(site)
		try:
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "movie_join")))
			parsing(driver.page_source)
			
			for i in range(2, 100):
				link = driver.find_elements_by_link_text(str(i))
				if len(link) > 0:
					link[0].click()
					parsing(driver.page_source)
				else:
					break
				#html = driver.page_source
		finally:
			print("===========DAUM    END==============")

	driver.close()
	driver.quit()
