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

def RT():
	driver = webdriver.PhantomJS('/home/ec2-user/temp2/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
	list = ['https://www.rottentomatoes.com/browse/opening', 'https://www.rottentomatoes.com/browse/in-theaters','https://www.rottentomatoes.com/browse/upcoming']
	for site in list:
		driver.get(site)
		try:
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "movie_info")))
			html = driver.page_source
			soup = BeautifulSoup(html, "html.parser")
			info = soup.find_all("div", {"class" : "movie_info"})
			for item in info:
				name = item.find("h3", {"class" : "movieTitle"})
				point = item.find_all("span", {"class" : "tMeterScore"})
				releasedatetag = item.find("p", {"class" : "release-date"})
				releasedate = releasedatetag.text
				releasedate = releasedate.replace("In Theaters ", "")
				rdate = parse(releasedate)
				if len(point) == 0:
					pointtext = ''
				else:
					pointtext = point[len(point) - 1].text.strip()

				save(name.text.strip(), rdate, pointtext, 'RT')	
		finally:
			print("===============RT  END==============")
			
	driver.close()
	driver.quit()
