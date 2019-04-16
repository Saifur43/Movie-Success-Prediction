from bs4 import BeautifulSoup
from urllib import request
from .models import Star, Movies, Director, Genre
import youtube_dl
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def imdb_scrapper():
    url = "https://www.imdb.com/movies-coming-soon/?ref_=nv_mv_cs"
    # page = requests.get(url)
    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    movie_list = soup.find('div', class_='list detail')

    movies1 = movie_list.find_all('div', class_='list_item odd')
    movies2 = movie_list.find_all('div', class_='list_item even')

    for movie in movies1:
        name_data = movie.find_all('a')[1]
        namex = name_data.text
        x = (namex.split('('))
        year_data = x[1]
        year = year_data[0:-1]
        name = x[0][1:-1]
        link = "https://www.imdb.com" + str(name_data.get('href'))
        info = movie.find('p', class_='cert-runtime-genre')

        run_time = info.find('time')
        genres = info.find_all('span')
        metarate = movie.find('div', class_='rating_txt')
        outline = movie.find('div', class_='outline')
        directors = movie.find('div', class_='txt-block')
        director = directors.find('a').text
        director_link = "https://www.imdb.com" + str(directors.find('a').get('href'))
        stars_info = movie.find_all('div', class_='txt-block')[1]
        stars = stars_info.find_all('a')
        img = movie.find('img', class_='poster shadowed')

        if Movies.objects.filter(name=name).exists():
            continue
        else:
            new_movie = Movies()
            new_movie.name = name
            new_movie.link = link
            new_movie.year = year
            new_movie.outline = outline.text
            new_movie.image = img.get('src')
            new_movie.yt_trailer_views = 0
            new_movie.yt_trailer_like = 0
            new_movie.yt_trailer_dislike = 0

            # IMDB meta score
            try:
                print(type(int(metarate.find('span').text)))
                new_movie.imdb_meta = int(metarate.find('span').text)
            except:
                new_movie.imdb_meta = 0
            # Runtime
            try:
                new_movie.runtime = run_time.text
            except:
                new_movie.runtime = 0

            # Director Data Input
            new_director = Director()
            if Director.objects.filter(d_name=director).exists():
                continue
            else:
                new_director.d_name = director
                new_director.weight = 0.000
                new_director.director_link = director_link
                new_director.save()
                new_movie.director = new_director

            new_movie.save()

            # Genres Data Input

            for genre in genres:
                new_genre = Genre()

                if Genre.objects.filter(g_name=genre.text).exists():
                    continue
                else:
                    if genre.text == "|":
                        continue
                    else:
                        new_genre.g_name = genre.text
                        new_genre.weight = 0.000
                        new_genre.save()
                        new_movie.genres.add(new_genre)
                        new_movie.save()

            # Stars Data Input

            for star in stars:
                new_star = Star()

                if Star.objects.filter(s_name=star.text).exists():
                    continue
                else:
                    new_star.s_name = star.text
                    new_star.weight = 0.000
                    new_star.star_link = "https://www.imdb.com" + str(star.get('href'))
                    new_star.save()
                    new_movie.stars.add(new_star)
                    new_movie.save()

        new_movie.save()

    # Second List
    for movie in movies2:
        name_data = movie.find_all('a')[1]
        namex = name_data.text
        x = (namex.split('('))
        year_data = x[1]
        year = year_data[0:-1]
        name = x[0][1:-1]
        link = "https://www.imdb.com" + str(name_data.get('href'))
        info = movie.find('p', class_='cert-runtime-genre')

        run_time = info.find('time')
        genres = info.find_all('span')
        metarate = movie.find('div', class_='rating_txt')
        outline = movie.find('div', class_='outline')
        directors = movie.find('div', class_='txt-block')
        director = directors.find('a').text
        director_link = "https://www.imdb.com" + str(directors.find('a').get('href'))
        stars_info = movie.find_all('div', class_='txt-block')[1]
        stars = stars_info.find_all('a')
        img = movie.find('img', class_='poster shadowed')

        if Movies.objects.filter(name=name).exists():
            continue
        else:
            new_movie = Movies()
            new_movie.name = name
            new_movie.link = link
            new_movie.year = year
            new_movie.outline = outline.text
            new_movie.image = img.get('src')
            new_movie.yt_trailer_views = 0
            new_movie.yt_trailer_like = 0
            new_movie.yt_trailer_dislike = 0

            # IMDB meta score
            try:
                print(type(int(metarate.find('span').text)))
                new_movie.imdb_meta = int(metarate.find('span').text)
            except:
                new_movie.imdb_meta = 0
            # Runtime
            try:
                new_movie.runtime = run_time.text
            except:
                new_movie.runtime = 0

            # Director Data Input
            new_director = Director()
            if Director.objects.filter(d_name=director).exists():
                continue
            else:
                new_director.d_name = director
                new_director.weight = 0.000
                new_director.director_link = director_link
                new_director.save()
                new_movie.director = new_director

            new_movie.save()

            # Genres Data Input

            for genre in genres:
                new_genre = Genre()

                if Genre.objects.filter(g_name=genre.text).exists():
                    continue
                else:
                    if genre.text == "|":
                        continue
                    else:
                        new_genre.g_name = genre.text
                        new_genre.weight = 0.000
                        new_genre.save()
                        new_movie.genres.add(new_genre)
                        new_movie.save()

            # Stars Data Input

            for star in stars:
                new_star = Star()

                if Star.objects.filter(s_name=star.text).exists():
                    continue
                else:
                    new_star.s_name = star.text
                    new_star.star_link = "https://www.imdb.com" + str(star.get('href'))
                    new_star.weight = 0.000
                    new_star.save()
                    new_movie.stars.add(new_star)
                    new_movie.save()

        new_movie.save()


def get_yt_info():
    def _get_youtube_video_info(url):
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url)

    mov_objs = Movies.objects.all()

    for movie in mov_objs:
        title = str(movie.name) + " official trailer"
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path='E:\geckodriver.exe')
        driver.get("https://duckduckgo.com/")
        driver.find_element_by_xpath("//input[@name='q']").send_keys(str(title))
        driver.find_element_by_id("search_button_homepage").click()

        print(driver.title)
        data = driver.find_element_by_xpath("//div[@id='r1-0']//a[contains(@class,'result__check')]")
        url = data.get_attribute('href')
        print(url)
        driver.quit()

        info = _get_youtube_video_info(url)
        movie.yt_trailer_title = info['title']
        movie.save()
        movie.yt_trailer_url = url
        movie.yt_trailer_views = int(info['view_count'])
        movie.yt_trailer_like = int(info['like_count'])
        movie.yt_trailer_dislike = int(info['dislike_count'])
        movie.yt_trailer_uploader = info['uploader']

        movie.save()


