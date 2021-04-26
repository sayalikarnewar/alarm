from script import set_form, set_alarm, all_alarm

def routes(app):
    
    #all alarm
    app.router.add_get('/all', all_alarm)

    #set alarm
    app.router.add_get('/set', set_form)
    app.router.add_post('/set', set_alarm, name='set_alarm')