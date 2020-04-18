from selenium import webdriver
from time import sleep
from smtplib import SMTP
from credentials import email, password

class Coronavirus():
		def __init__(self):
				self.driver = webdriver.Chrome()
				

		def get_data(self):
			country_element = "India"
			sleep(4)
			search_field = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today_filter"]/label/input')
			sleep(2)
			search_field.send_keys(country_element)
			row = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]/tr')
			data = row.text.split(" ")
			total_cases = data[1]
			new_cases = data[2]
			total_deaths = data[3]
			new_deaths = data[4]
			total_recovered = data[5]
			active_cases = data[6]
			server = SMTP('smtp.gmail.com', 587)
			server.ehlo()
			server.starttls()
			server.ehlo()
			server.login(email, password)
			subject = 'Coronavirus stats in your country today!'
			body = 'Today in ' + country_element + '\
			\nThere is new data on coronavirus:\
			\nTotal cases: ' + total_cases +'\
			\nNew cases: ' + new_cases + '\
			\nTotal deaths: ' + total_deaths + '\
			\nNew deaths: ' + new_deaths + '\
			\nActive cases: ' + active_cases + '\
			\nTotal recovered: ' + total_recovered + '\
			\nCheck the link: https://www.worldometers.info/coronavirus/'
			msg = f"Subject: {subject}\n\n{body}"
			server.sendmail('Coronavirus',email,msg)
			print('Hey Email has been sent!')
			server.quit()

bot = Coronavirus()
bot.driver.get('https://www.worldometers.info/coronavirus/')

bot.get_data()