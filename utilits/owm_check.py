
import aiohttp
import asyncio
from utilits.RangeDict import RangeDict

wind_direction_dict = RangeDict({range(0, 23): 'северный', range(23, 67): 'северовосточный',
                                range(67, 112): 'восточный', range(112, 157): 'юговосточный',
                                range(157, 202): 'южный', range(202, 247): 'югозападный',
                                range(247, 292): 'западный', range(292, 315): 'северозападный',
                                range(315, 361): 'северный'})

async def owm(location):
    url = rf'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=07c8001ef0edd2097a8484787beae918&lang=ru&units=metric'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.json()
        place = html['name']
        weather_description = html['weather'][0]['description']
        temp_current = html['main']['temp']
        humidity = html['main']['humidity']
        pressure = html['main']['pressure']*0.75
        wind_degrees = html['wind']['deg']
        wind_direction = wind_direction_dict[wind_degrees]
        wind_speed = html['wind']['speed']
        #gust_speed = html['wind']['gust']
        answer = f'''{place} 
{weather_description.capitalize()}, температура на улице:  {round(temp_current)}  градусов.
Влажность: {humidity}%, давление {round(pressure)} ммрст.
Ветер {wind_direction}, скорость {wind_speed} м/c'''

        return answer

