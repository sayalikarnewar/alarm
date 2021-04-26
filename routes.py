from script import set_form, set_alarm

def routes(app):
    
    #set alarm
    app.router.add_get('/', set_form)
    app.router.add_post('/', set_alarm, name='set_alarm')