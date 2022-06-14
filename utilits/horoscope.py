from bs4 import BeautifulSoup
import aiohttp


async def horoscope_pars(zodiac_sing_ru):
    zodiac_href_built = {"Овен": 'oven', "Телец": 'telets', "Близницы": 'bliznetsi', "Рак": 'rac', "Лев": 'lev',
                         "Дева": 'deva', "Весы": 'vesy', "Скорпион": 'scorpion', "Стрелец": 'strelets',
                         "Козерог": 'kozerog', "Водолей": 'vodoley', "Рыбы": 'riby'}
    if zodiac_sing_ru in zodiac_href_built:
        url = ('https://www.astrostar.ru/horoscopes/main/' + zodiac_href_built[zodiac_sing_ru] + '/day.html')

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                html = await response.text()
                soup = BeautifulSoup(html, 'lxml')
                divs = soup.find_all('p')
            answer_z_sing = divs[0].text + '\n' + divs[1].text + '\n' + divs[2].text
        return answer_z_sing
    else:
        return 'Выбери знак зодака из списка'
