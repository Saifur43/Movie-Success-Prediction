from selenium import webdriver
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='E:\geckodriver.exe')
driver.get("https://www.prothomalo.com/bangladesh/article/1588013/%E0%A6%9C%E0%A6%BE%E0%A6%B9%E0%A6%BE%E0%A6%B2%E0%A6%AE%E0%A6%95%E0%A7%87-%E0%A6%A6%E0%A7%87%E0%A6%96%E0%A6%A4%E0%A7%87-%E0%A6%9A%E0%A6%BE%E0%A6%A8-%E0%A6%B9%E0%A6%BE%E0%A6%87%E0%A6%95%E0%A7%8B%E0%A6%B0%E0%A7%8D%E0%A6%9F")

print(driver.find_element_by_xpath("//h1[@class='title mb10']").text)
print(driver.find_element_by_xpath("//span[@itemprop='datePublished']").text)
print(driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/article[1]/div[1]/p[1]/a[1]/span[1]/img[1]").get_attribute('src'))

driver.quit()