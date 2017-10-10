import re
import time
from selenium import webdriver

def FindNumberOfQueries(htmlData):
    queryData1 = re.findall('First-Person',str(htmlData))
    queryData2 = re.findall('FPS',str(htmlData))
    count = 0
    count = len(queryData1)+len(queryData2)-2 #remove garbage values from webpage , always 2 on menu
    return count

def WriteToTextfile(numberOfQueries,i):
    #read previous sum
    file = open('counter.txt', 'r')
    previousNumber = object()
    previousNumber = file.read()
    print(previousNumber)
    file.close()
    #add newly found to the sum and write on file
    file = open('counter.txt', 'w')
    numberOfQueries += int(previousNumber)
    file.write(str(numberOfQueries))
    file.close()

driver = webdriver.Chrome("C:/Users/lalai/Desktop/chromedriver.exe") #add path variable
driver.get("https://vrgamesfor.com/list/")

numberOfPages=227 #change to search until button not found
for i in range(numberOfPages):
    queriesFound = FindNumberOfQueries(driver.page_source)
    WriteToTextfile(queriesFound,i)
    #click on button and wait to load
    element=driver.find_element_by_css_selector('.next-btn > span:nth-child(1)')
    driver.execute_script("arguments[0].click();", element)
    time.sleep(10.0)
    i+=1
    







