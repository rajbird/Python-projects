import time
import pandas as pd
from html.parser import HTMLParser
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/Rajbir/chromedriver')

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def doBlocking(url):
    # Go to your page url
    driver.get(url)
    time.sleep(7)

    try:
        test = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/span')
        time.sleep(6)
        s = MLStripper()
        s.feed(test.get_attribute("innerHTML"))
        info = s.get_data()
        if(info == "Blocked"):
            return "user is already blocked"
        return blockUser(driver)
    except Exception as e:
        return blockUser(driver)


def blockPrivateUser(driver):
    try:
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div').click()
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[1]').click()
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div[3]/div[2]/div').click()
        time.sleep(1)
        return "blocked"
    except Exception as e:
      eMsg = f"ERROR: {e}"
      return eMsg

def blockUser(driver):
    print("user is protected")
    time.sleep(1)
    try:
      driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div/div[1]/div').click()
      time.sleep(1)

      driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/div[3]/div/div/div/div[3]').click()
      time.sleep(1)

      driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div').click()
      time.sleep(1)
      return "blocked"
    except Exception as e:
        eMsg = f"ERROR: {e}"
        try:
            text = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/div[1]/span').get_attribute("innerHTML")
            if(text == 'These Tweets are protected'):
                return blockPrivateUser(driver)
            return eMsg
        except:
            return eMsg


def login():
    # Go to your page url
    driver.get('https://twitter.com/login')
    email = '' #provide email
    pword = '' #provide password
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input").send_keys(email)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input").send_keys(pword)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div").click()
    time.sleep(1)

login()
df = pd.read_excel('mini.xlsx') # can also index sheet by name or fetch all sheets
users = df['Screen Name'].tolist()
blocking = []

for user in users:
    url = 'https://twitter.com/' + user
    print(url)
    rtn = doBlocking(url)
    print(rtn)
    blocking.append(rtn)

df['Blocked'] = blocking
df.to_excel("result.xlsx",index=False)

#driver.quit()
print('\ndone')




#login()
# Go to your page url
#driver.get('https://twitter.com/prettyjoonie')
#time.sleep(1)
