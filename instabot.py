from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
	def __init__(self,username,password):
		self.username = username
		self.password = password
		self.bot      = webdriver.Firefox(executable_path = 'C:/Users/Saif Ullah Awais/AppData/Local/Programs/Python/Python38-32/geckodriver.exe')

	def login(self):
		bot = self.bot
		bot.get('https://www.instagram.com/accounts/login')
		time.sleep(3)
		bot.find_element_by_name('username').send_keys(self.username)
		bot.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
		time.sleep(3)

	def searchHashtag(self,hashtag):
		bot = self.bot

		bot.get('https://www.instagram.com/explore/tags/' + hashtag)

	def likePhotos(self,amount):
		bot = self.bot
		bot.find_element_by_class_name('v1Nh3').click()

		i = 1
		while i <= amount:
			time.sleep(12)
			bot.find_element_by_class_name('fr66n').click()
			bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			
			i += 1

		bot.get('https://instagram.com/' + self.username)

insta =InstagramBot('USER__NAME', 'PASSWORD')
insta.login()
insta.searchHashtag("memesindia")
insta.likePhotos(1000)