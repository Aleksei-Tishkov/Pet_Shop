from random import randrange, randint, sample, choice

from django.db import models

from django.core.cache import cache
from django.db.models import QuerySet


def get_random_instance(query):
    return query[randint(0, query.__len__()-1)]


def get_random_instances(query: QuerySet, times: int) -> list:
    instances = list(query)
    if times > query.__len__():
        for _ in range(times):
            instances.append(choice(query))
    else:
        for _ in range(times):
            instances = sample(instances, times)
    return instances








