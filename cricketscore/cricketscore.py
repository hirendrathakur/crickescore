from HTMLParser import HTMLParser
import urllib
from bs4 import BeautifulSoup
import subprocess
import time
import os

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
		previous_runs = 0
		previous_wickets = 0
		while(True):
			current_score = self.get_score()
			split_list = current_score.split('/')
			current_runs = split_list[0]
			current_wickets = split_list[1].split(" ")[0]
			print current_score
			if previous_score!=current_score:
				previous_score = current_score
				base_dir = os.path.dirname(os.path.abspath(__file__))
				self.image_path = base_dir+"/cricket.png"

				if previous_runs!=current_runs:
					previous_runs = current_runs
					self.image_path = base_dir+"/bat.jpg"
				if previous_wickets!=current_wickets:
					previous_wickets = current_wickets
					self.image_path = base_dir+"/out.png"

				subprocess.Popen(['notify-send','-i',self.image_path,'Cricket Score',current_score])
				time.sleep(5)

if __name__ == '__main__':
	CricketScore()

