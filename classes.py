# 1. Change the directory of the chromedriver acording to the os.
# 2. Add email_id and password.
# 3. Check the variables for class.
# 4. If you're adding class meet link right click on the link inspect element them right click on the code and then click on copy then xpath, add then add the link to the specified variable
#
# Author: Vitthal Gupta 
#
# Timetable according to IIIT Bhubneswar EEE 4th Semester
#
#

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
from datetime import date

# Change e-mail id and password

email_id_user = '<--! Email ID -->'
password_user = '<--! Password -->'

# Appointing the epoch time

seconds = time.time()

#Gives the time value to the result variable

result = time.localtime(seconds)

#Loads chrome with default settings

opt=Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})
def join_class(class_name):
	#Gives path to chrome webdriver and loads classroom webpage 
	#Change the path according to your os
	driver=webdriver.Chrome(options=opt, executable_path='/home/phoenix/Documents/College/automation/chromedriver')
	driver.get('https://accounts.google.com/ServiceLogin/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2F&followup=https%3A%2F%2Fclassroom.google.com%2F&emr=1&flowName=GlifWebSignIn&flowEntry=AddSession')

	#Logs in the classroom
	username=driver.find_element_by_id('identifierId')
	username.click()
	username.send_keys(email_id_user)

	next=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
	next.click()
	time.sleep(2)
	password=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
	password.click()
	password.send_keys(password_user)


	next=driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
	next.click()

	time.sleep(15)

	#Finds the classroom
	classroom=driver.find_element_by_xpath(class_name)
	classroom.click()


	time.sleep(5)

	classwork = driver.find_element_by_xpath('//*[@id="yDmH0d"]/nav/div[1]/div[2]/div/div[2]/a')
	classwork.click()
	time.sleep(2)

	link=driver.find_element_by_xpath('//*[@id="c0"]/div/div/div[1]/div[2]/span/div[1]/a/span/span/span')
	link.click()

	time.sleep(2)


	#Switches the tab
	#driver.switch_to.window(driver.window_handles[1])
	current_tab=driver.window_handles[1]
	driver.switch_to.window(current_tab)

	#print(driver.title)

	time.sleep(5)

	#Turns off mic and camera and joins the meet
	camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div/span')
	camera.click()
	time.sleep(1)
	mic=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div/span')
	mic.click()
	time.sleep(1)
	join=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span')
	join.click()
	time.sleep(15)
	driver.quit()

#Variable for the classes x-path

# CS-IV- Prof. S Ganguly
com_eng = '//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[2]/div[1]/div[3]/h2/a[1]/div[1]'
# DEC Lab - P.R. Meher
dec_lab = '//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]'
# PASP - Prof. R.K. Nayak 
pasp = '//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[4]/div[1]/div[3]/h2/a[1]/div[1]'
# EEM - Prof. A.P. Hota
eem = ''
# DEC- Prof. S.k Mohanty
dec = '//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[3]/div[1]/div[3]/h2/a[1]/div[1]'
# EMFW- Prof. U.R. Raut
emfw = '//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[5]/div[1]/div[3]/h2/a[1]/div[1]'
# EM-1- Prof. U. Subudhi
em_1 = '//*[@id="yDmH0d"]/div[2]/div[1]/div[2]/div/ol/li[6]/div[1]/div[3]/h2/a[1]/div[1]'
# EM-1-Lab- Prof. S.P. Sahoo
em_1_lab = ''
# EEM-Lab- Prof. S.P. Sahoo
eem_lab = ''

#Conditional Functions for joining the class

#TEST
#if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 4:
#	if result.tm_hour == 15:
#		if result.tm_min in range (8,15):
#			join_class(com_eng)

# CS-IV- Prof. S Ganguly ( Weekday Friday only)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 4:
	if result.tm_hour == 15:
		if result.tm_min in range (8,15):
			join_class(com_eng)

# DEC Lab - P.R. Meher
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 0:
	if result.tm_hour == 15:
		if result.tm_min in range (8,15):
			join_class(dec_lab)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 0:
	if result.tm_hour == 16:
		if result.tm_min in range (8,15):
			join_class(dec_lab)

# PASP - Prof. R.K. Nayak
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 0:
	if result.tm_hour == 10:
		if result.tm_min in range (0,10):
			join_class(pasp)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 2:
	if result.tm_hour == 10:
		if result.tm_min in range (0,10):
			join_class(pasp)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 4:
	if result.tm_hour == 10:
		if result.tm_min in range (0,10):
			join_class(pasp)

# EEM - Prof. A.P. Hota
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 0:
	if result.tm_hour == 11:
		if result.tm_min in range (5,15):
			join_class(eem)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 3:
	if result.tm_hour == 14:
		if result.tm_min in range (0,10):
			join_class(eem)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 4:
	if result.tm_hour == 11:
		if result.tm_min in range (5,15):
			join_class(eem)

# DEC- Prof. S.k Mohanty
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 0:
	if result.tm_hour == 12:
		if result.tm_min in range (0,10):
			join_class(dec)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 1:
	if result.tm_hour == 12:
		if result.tm_min in range (0,10):
			join_class(dec)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 2:
	if result.tm_hour == 14:
		if result.tm_min in range (0,10):
			join_class(dec)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 3:
	if result.tm_hour == 11:
		if result.tm_min in range (5,15):
			join_class(dec)

# EMFW- Prof. U.R. Raut
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 0:
	if result.tm_hour == 14:
		if result.tm_min in range (0,10):
			join_class(emfw)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 1:
	if result.tm_hour == 11:
		if result.tm_min in range (5,15):
			join_class(emfw)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 2:
	if result.tm_hour == 11:
		if result.tm_min in range (5,15):
			join_class(emfw)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 3:
	if result.tm_hour == 14:
		if result.tm_min in range (0,10):
			join_class(emfw)

# EM-1- Prof. U. Subudhi
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 1:
	if result.tm_hour == 10:
		if result.tm_min in range (0,10):
			join_class(em_1)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 2:
	if result.tm_hour == 12:
		if result.tm_min in range (10,20):
			join_class(em_1)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 3:
	if result.tm_hour == 12:
		if result.tm_min in range (10,20):
			join_class(em_1)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 4:
	if result.tm_hour == 12:
		if result.tm_min in range (10,20):
			join_class(em_1)

# EM-1-Lab- Prof. S.P. Sahoo
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 1:
	if result.tm_hour == 14:
		if result.tm_min in range (0,10):
			join_class(em_1_lab)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 1:
	if result.tm_hour == 15:
		if result.tm_min in range (0,10):
			join_class(em_1_lab)

# EEM-Lab- Prof. S.P. Sahoo
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 2:
	if result.tm_hour == 15:
		if result.tm_min in range (5,15):
			join_class(em_1_lab)
if date(result.tm_year,result.tm_mon,result.tm_mday).weekday() == 2:
	if result.tm_hour == 16:
		if result.tm_min in range (5,15):
			join_class(em_1_lab)