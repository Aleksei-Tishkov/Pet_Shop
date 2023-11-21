from random import randrange, randint

from django.db import models


def get_random_instance(query):
    return query[randint(0, query.__len__()-1)]


