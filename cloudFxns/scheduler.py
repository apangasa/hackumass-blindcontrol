import time
import requests


# Takes in a schedule dictionary and sends instructions at specified times
# Exits when mode is changed to manual
def send_instructions(schedule):
    manual = False
    while not manual:
        for scheduled_time in schedule.keys():
            if int(time.strftime('%H')) == int(scheduled_time.split(':')[0]) and int(time.strftime('%M')) == int(scheduled_time.split(':')[1]):
                new_state = schedule[scheduled_time]
                print('Posting... ' + str(new_state))
                requests.post(
                    'https://blind-control-299118.ue.r.appspot.com/flip', json={'new_state': new_state})
                print('Posted.')

        manual = True if requests.get('https://blind-control-299118.ue.r.appspot.com/get-mode').json()[
            'mode'] == 'manual' else False
        schedule = requests.get(
            'https://blind-control-299118.ue.r.appspot.com/get-schedule').json()
    return


def create_schedule(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()

    send_instructions(request_json)

    return 'Success!'
