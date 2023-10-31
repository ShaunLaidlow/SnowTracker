from bs4 import BeautifulSoup
import requests

#Link to website that tracker scrapes. Linked currently to a specific mountain
#website = "https://www.snow-forecast.com/resorts/Whistler-Blackcomb/6day/top"
website = "https://www.snow-forecast.com/resorts/Andermatt/6day/mid"

#Gets html from website
response = requests.get(website)
web_text = response.text

#Uses Beautiful soup to parse the website, finds snow-report table
soup = BeautifulSoup(web_text, "html.parser")
snow_report = soup.find(class_="snow-depths-table__table")

#Determines snow height at top of mountain
top_snow_depth = snow_report.find('th', string="Top snow depth:").find_next('td')
top_snowht = top_snow_depth.find('span', {'class': 'snowht'}).get_text()
top_snowu = top_snow_depth.find('span', {'class': 'snowu'}).get_text()

#Determines snow height at bottom of mountain
bot_snow_depth = snow_report.find('th', string="Bottom snow depth:").find_next('td')
bot_snowht = top_snow_depth.find('span', {'class': 'snowht'}).get_text()
bot_snowu = top_snow_depth.find('span', {'class': 'snowu'}).get_text()

#Determines amount of fresh snow
fresh_snow_depth = snow_report.find('th', string="Fresh snowfall depth:").find_next('td')
fresg_snowht = top_snow_depth.find('span', {'class': 'snowht'}).get_text()
fresh_snowu = top_snow_depth.find('span', {'class': 'snowu'}).get_text()

#Determines last known date of snowfall
last_snow_date = snow_report.find('th', string="Last snowfall:").find_next('td').get_text()







