import time
import requests


# Takes in a schedule dictionary and sends instructions at specified times
# Exits when mode is changed to manual
def scheduler(schedule):
    manual = False
    while not manual:
        for scheduled_time in schedule.keys():
            if int(time.strftime('%H')) == int(scheduled_time.split(':')[0]) and int(time.strftime('%M')) == int(scheduled_time.split(':')[1]):
                new_state = schedule[scheduled_time]
                requests.post('FLIP STATE', json={'new_state': new_state})

        manual = True if requests.get('GET MODE').json()[
            'mode'] == 'manual' else False
        schedule = requests.get('GET SCHEDULE').json()
