from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os.path
from os import path

class SetupTest:
    def __init__(self):
        self.test_file = null #file location object
        self.logs_file = null #file location object
        self.test = null #array of test commands

    def createTestFile():
        print("SetupTest.createTestFile")
        if os.path.isfile('test.txt') == False:
          open('test.txt',"a")

        if os.path.isfile('logs.txt') == False:
          open('logs.txt',"a")

    def openScript():
        print("SetupTest.openScript")
        SetupTest.createTestFile()

        test_path = 'test.txt'
        SetupTest.test_file = open(test_path,'r')
        SetupTest.test = SetupTest.test_file.readlines()

        logs_path = 'logs.txt'
        SetupTest.logs_file = open(logs_path,'w')

        title = 'Steps:\n'
        SetupTest.logs_file.write(title)
        print(title)

        SetupTest.logs_file.writelines(SetupTest.test)
        print(SetupTest.test)

        logs = 'Logs:\n'
        SetupTest.logs_file.write(logs)
        print(logs)

    def closeScript():
        print("SetupTest.closeScript")
        SetupTest.test_file.close()
        SetupTest.logs_file.close()

class RunTest:
    def URL():
        URL = str(test.split("|")[1])
        URLassert = str(test.split("|")[2].replace("\n", ""))
        browser.get(URL)
        print(URLassert)
        assert URLassert in browser.title #check browser title = URLassert
        SetupTest.logs_file.write("Search for " + URL + " in Browser\n") #Logs

    def TEXTBOX():
        field = str(test.split("|")[1].replace("\n", ""))
        print(field)
        elem = browser.find_element_by_name(field)  # Find the search box
        elem.send_keys('seleniumhq' + Keys.RETURN)
        SetupTest.logs_file.write("Search for textbox with name = " + field + "\n") #Logs

    def SLEEP():
        time.sleep(int(test.split("|")[1]))
        SetupTest.logs_file.write("wait for " + str(test.split("|")[1].replace("\n", "")) + " seconds\n") #Logs


if __name__ == "__main__":
    #read script and extract commands
    SetupTest.openScript()
    print(SetupTest.test_file.name, SetupTest.logs_file.name)
    testScript = SetupTest.test # grab the test script
    browser = webdriver.Firefox()
    i=0
    for test in testScript: #Read commands in file and execute them
        SetupTest.logs_file.write(test)
        if "URL|" in test: #check for URL and search URL
            RunTest.URL()
        if "TEXTBOX|" in test:
            RunTest.TEXTBOX()
        if "SLEEP|" in test: #wait a set time in seconds before moving on
            RunTest.SLEEP()
        i+=1
    browser.quit()
    SetupTest.closeScript()
