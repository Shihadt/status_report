from selenium import webdriver
#from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
#from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select

def read_data(file_name):
	inp = open(file_name)
	text = ""
	for line in inp:
		line = line.strip()
		text=text + " " + line
	return text

def confirmation(driver):
	print "Do you want to post status report on space(yes/no)"
	ans = raw_input()
	if ans == "yes":
		driver.find_element_by_id('saveDailyStatusButton').click()
	else:
		raw_input("press enter to exit")

def wait_for_ajax(my_driver):
	wait = WebDriverWait(my_driver, 15)
	try:
		wait.until(lambda my_driver: my_driver.find_element_by_id('activityType'))
		wait.until(lambda my_driver: my_driver.execute_script('return jQuery.active') == 0)
		wait.until(lambda my_driver: my_driver.execute_script('return document.readyState') == 'complete')
	except Exception as e:
		pass
def main_fun():
	options = webdriver.ChromeOptions()
#	options.add_argument("user-data-dir=home/ShihaD/.config/google-chrome/Default") #Path to your chrome profile
	options.add_argument("user-data-dir=/home/ShihaD/.config/google-chrome/Default")	
	options.add_argument('--no-sandbox')
	options.add_argument('--disable-dev-shm-usage')
	#options.add_argument('--headless')

	driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)
	driver.get('https://space.qburst.com/l/#/dailyStatus/apply')
	wait_for_ajax(driver)
	#element = driver.find_element_by_id('//selectactivityType')
	print "helloo"
	#element = driver.find_element_by_xpath("//select[@name='activityType']/option[value()=5]").click()
	select = Select(driver.find_element_by_id('activityType'))
	select.select_by_value('1')
	text = read_data('/home/ShihaD/Documents/shihad/work/amail/work_done.txt')
	driver.find_element_by_id("message").clear()
	driver.find_element_by_id('message').send_keys(text)
	return driver

driver = main_fun()
confirmation(driver)
