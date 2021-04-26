import aiohttp_jinja2
import time
import datetime
import os


@aiohttp_jinja2.template('set_alarm.html')
async def set_form(request):
    return {}

@aiohttp_jinja2.template('set_alarm.html')
async def set_alarm(request):
    form = await request.post()
    
    date = form['date'].split('-')
    hour = int(form['hour'])
    minute = int(form['minute'])
    name = str(form['name'])

    try:
        file = str(form['filename'].filename)
        file_ = str(file)

        print('Please wait...')

        for root, dirs, files in os.walk('/home/'):
            for name in files:
                if file_ in name:
                    path = os.path.abspath(os.path.join(root, name))
                    print('file found!! Wait for the alarm!')
                    break
            
    except:
        return {"response": "no such file found"}


    try:
        now = datetime.datetime.strftime(datetime.datetime.today() , '%Y-%m-%d %H:%M:%S')
        alarm = str(datetime.datetime(int(date[0]), int(date[1]), int(date[2]), hour, minute, 0))

        if now>alarm:
            return {'response' : 'Set the time in future.'}

        while True:
            time.sleep(1)
            now = datetime.datetime.strftime(datetime.datetime.today() , '%Y-%m-%d %H:%M:%S')
            print(now)
            
            if now==alarm:
                os.system("mpg123 " + path)
                print('oopps')
                time.sleep(4)
                return {'response' : 'Wake up! \n' + name}

        
    except Exception as e:
        return {'response' : 'Error setting alarm' + str(e)}

