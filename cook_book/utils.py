from django.db import DatabaseError
from functools import wraps
from django.http import HttpResponse


def handle_db_errors(func):

    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DatabaseError:
            return HttpResponse('Sorry, service unavailable now', status=500)

    return inner
