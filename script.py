import aiohttp_jinja2
import time
import datetime
from playsound import playsound
import os

'''
all alarms
'''


@aiohttp_jinja2.template('set_alarm.html')
async def set_form(request):
    return {}

@aiohttp_jinja2.template('set_alarm.html')
async def set_alarm(request):
    form = await request.post()
    date = form['date'].split('-')
    hour = int(form['hour'])
    minute = int(form['minute'])
    second = int(form['second'])

    db = request.app['db']

    try:
        alarm = str(datetime.datetime(int(date[0]), int(date[1]), int(date[2]), hour, minute, second))

        while True:
            time.sleep(1)
            now = datetime.datetime.strftime(datetime.datetime.today() , '%Y-%m-%d %H:%M:%S')
            print(now)
            if now>alarm:
                return {'response' : 'Set the time in future.'}
            elif now==alarm:
                file = "/home/sayali_karnewar/Documents/Projects/alarm-clock/media/Naruto.mp3"
                os.system("mpg123 " + file)
                time.sleep(10)
                return {'response' : 'Wake up!'}

        
    except Exception as e:
        return {'response' : 'Error setting alarm' + str(e)}


@aiohttp_jinja2.template('all_alarm.html')
async def all_alarm(request):
    db = request.app['db']
    
    return {}
