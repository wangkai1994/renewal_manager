from django.apps import AppConfig


class RenewalConfig(AppConfig):
    name = 'renewal'

from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
    layout = 'horizontal'
