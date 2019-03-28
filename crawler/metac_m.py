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

def METAC_M():
	driver = webdriver.PhantomJS('/home/ec2-user/temp2/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
	list = ['https://www.metacritic.com/browse/movies/release-date/theaters']
	for site in list:
		driver.get(site)
		try:
			WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME , "clamp-list")))
			html = driver.page_source
			soup = BeautifulSoup(html, "html.parser")
			info = soup.find_all("td", {"class" : "clamp-summary-wrap"})
			for item in info:
				name = item.find("h3")
				point = item.find("div", {"class" : "clamp-score-wrap"})
				releasedatetag = item.find("div", {"class" : "clamp-details"})
				releasedate = releasedatetag.find_all("span")[1].text
				rdate = parse(releasedate)
				if point.text.strip() == "tbd":
					pointtext = ''
				else:
					pointtext = point.text.strip()

				save(name.text.strip(), rdate, pointtext, "METAC")		
		finally:
			print("==========METAC    END==============")
			
	driver.close()
	driver.quit()
