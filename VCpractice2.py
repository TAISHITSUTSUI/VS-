from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://angel.co/company/braze")
href = driver.find_element_by_link_text("braze.com").get_attribute("href")
print('href:'+(href))
href = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[1]/div/ul/li[2]/ul/li[1]/a").get_attribute("href")
print('href:'+(href))
href = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[1]/div/ul/li[2]/ul/li[2]/a").get_attribute("href")
print('href:'+(href))
href = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[1]/div/ul/li[2]/ul/li[3]/a").get_attribute("href")
print('href:'+(href))
href = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[1]/div/ul/li[2]/ul/li[4]/a").get_attribute("href")
print('href:'+(href))

location1 = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[2]/ul/li[1]")
location2 = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[2]/ul/li[2]")
location3 = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/aside/div/div[1]/dl/dt[2]/ul/li[3]")

print('location1:'+(location1.text))
print('location2:'+(location2.text))
print('location3:'+(location3.text))