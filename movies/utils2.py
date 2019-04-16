from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from .models import Star, Director


def stars_update():
    stars = Star.objects.all()

    for star in stars:
        if star.insta_followers == 0:
            print(star.s_name)

            url = star.star_link
            # page = requests.get(url)
            options = Options()
            options.headless = True
            driver = webdriver.Firefox(options=options, executable_path='E:\geckodriver.exe')
            driver.get(url)
            try:
                x = driver.find_element_by_xpath("//span[contains(text(),'Actor')]").text
            except:
                x = driver.find_element_by_xpath("//span[contains(text(),'Actress')]").text

            if x == "Actor":

                try:
                    credit = driver.find_element_by_xpath("//div[@id='filmo-head-actor']").text
                    image = driver.find_element_by_xpath("//img[@id='name-poster']").get_attribute('src')
                    about = driver.find_element_by_xpath("//div[@class='inline']").text
                    credit = float(credit[13:16])

                    star.weight = credit
                    star.about = about
                    star.star_img = image
                except:
                    continue

            elif x == "Actress":
                try:
                    credit = driver.find_element_by_xpath("//div[@id='filmo-head-actress']").text
                    image = driver.find_element_by_xpath("//img[@id='name-poster']").get_attribute('src')
                    about = driver.find_element_by_xpath("//div[@class='inline']").text
                    credit = float(credit[15:18])
                    star.weight = credit
                    star.about = about
                    star.star_img = image
                except:
                    continue

            title = str(star.s_name) + " instagram"

            driver.get("https://duckduckgo.com/")
            driver.find_element_by_xpath("//input[@name='q']").send_keys(str(title))
            driver.find_element_by_id("search_button_homepage").click()
            data = driver.find_element_by_xpath("//div[@id='r1-0']//a[contains(@class,'result__check')]")
            star.star_insta = data.get_attribute('href')

            try:
                followers_data = driver.find_element_by_xpath(
                    "//div[contains(@class,'results js-results')]//div[1]//div[1]//div[2]").text
                followers_insta = followers_data.split(" ")
                followers = followers_insta[0]
                if followers[-1] == 'k':
                    followers = followers[:-1]
                    followers = float(followers) * 1000
                    star.insta_followers = int(followers)
                elif followers[-1] == 'm':
                    followers = followers[:-1]
                    followers = float(followers) * 1000000
                    star.insta_followers = int(followers)
                else:
                    followers = float(followers)
                    star.insta_followers = int(followers)
            except:
                continue

            driver.quit()
            try:
                star.save()
            except:
                continue

        else:
            continue


def director_update():
    directors = Director.objects.all()

    for director in directors:

        url = director.director_link

        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path='E:\geckodriver.exe')
        driver.get(url)

        try:

            credit = driver.find_element_by_xpath("//div[@id='filmo-head-director']").text
            image = driver.find_element_by_xpath("//img[@id='name-poster']").get_attribute('src')
            about = driver.find_element_by_xpath("//div[@class='inline']").text
            credit = float(credit[16:18])

            director.weight = credit
            director.about = about
            
            if director.id is None:
                director.d_img = "https://images-na.ssl-images-amazon.com/images/I/818%2BI9cEsEL._SY606_.jpg"
            director.save()

        except:
            continue

        driver.quit()
