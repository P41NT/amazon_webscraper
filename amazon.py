from selenium import webdriver

f = open('amazon.txt','r')
url_in = f.read()

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome("/Users/exploiter/Downloads/chromedriver", options=options)
urls = url_in.split(";")
for url in urls:
    driver.get(url)
    print("================================")
    print(driver.find_element_by_id("productTitle").text)
    try:
        print(driver.find_element_by_id("priceblock_dealprice").text)
    except:
        print(driver.find_element_by_id("priceblock_saleprice").text)

    print(driver.find_element_by_xpath("//*[contains(text(),'Top 100')]/..").text)
driver.close()
