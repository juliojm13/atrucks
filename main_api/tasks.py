from atrucks.celery import app
from main_api.parser import save_external_data


@app.task()
def save_data():
    """
    Saves data from an external service to the database every day.
    """
    save_external_data()
