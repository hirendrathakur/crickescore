from HTMLParser import HTMLParser
import urllib
from bs4 import BeautifulSoup
import subprocess
import time

class CricketScore():
	def __init__(self):
		self.url = 'http://www.cricbuzz.com/live-cricket-scores/16869/ind-vs-eng-2nd-test-   england-tour-of-india-2016-17'
		self.start_process()

	def get_score(self):
		html_obj = urllib.urlopen(self.url)
		html_string = html_obj.read().decode('utf-8')
		parsed_html = BeautifulSoup(html_string,'html.parser')
		result =  parsed_html.body.find('div',attrs={'class':'cb-min-bat-rw'}).text
		return result

	def start_process(self):
		previous_score = ''
		while(True):
			current_score = self.get_score()
			if previous_score!=current_score:
				previous_score = current_score
				print current_score
				subprocess.Popen(['notify-send','Cricket Score',current_score])
				time.sleep(5)

if __name__ == '__main__':
	CricketScore()

