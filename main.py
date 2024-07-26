from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time,threading

# Set up the Chrome driver
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run headless Chrome if you don't want the browser window to open
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL of the webpage you want to increase views for
url = 'https://x.com/chatgps_app/status/1816482323518366033'
# url="https://www.youtube.com/watch?v=rQm1QS0_dmU"
# url="https://chatgps.rf.gd"
# Number of views you want to simulate
print('start')
num_views = 5
def th_views():
    # driver.get(url)
    driver.execute_script("window.open('%s')"%url)
    # time.sleep(10)  # Wait for 2 seconds before loading the page again
th=['']*num_views
for i in range(num_views):
    # driver.get(url)
    # search = driver.find_element_by_id("search")
    # driver.execute_script("window.open('%s')"%url)
    # time.sleep(10) 
    th[i]=threading.Thread(target=th_views)
    th[i].start()
for i in range(num_views):
    th[i].join()
    print(f"View {i+1} completed")
time.sleep(120)
driver.quit()
