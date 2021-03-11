from enum import Enum
from django.utils.translation import ugettext_lazy as _


class ToyTypeEnum(Enum):
    ANIMALS = "animals"
    DOLLS = "dolls"
    CARS = "cars"
    EDUCATIONAL_TOYS = "educational_toys"
    ELECTRONIC_TOYS = "electronic_toys"

    @classmethod
    def get_value_tuples(cls):
        return ((item.value, _(item.value.replace("_", " ").title())) for item in cls)

    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)