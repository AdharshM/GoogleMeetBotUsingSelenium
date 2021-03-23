from selenium import webdriver

driver = webdriver.Chrome();

emailId = input('Enter your email Id : ')
password = input('Enter Password : ')
meetId = input('Enter the meet Id : ')

signIn = driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a')
signIn.click()

email = driver.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys(emailId)

next1 = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
next1.click()

pswd = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
pswd.send_keys(password)

next2 = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
next2.click()

meetCode = driver.find_element_by_xpath('//*[@id="i3"]')
meetCode.send_keys(meetId)

joinMeet = driver.find_element_by_path('//*[@id="yDmH0d"]/c-wiz/div[1]/div[2]/div/div[1]/div[3]/div[2]/div[2]/button/div[2]')
joinMeet.click()

#Enjoy



