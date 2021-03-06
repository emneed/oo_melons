"""This file should have our order classes in it."""
import random
import time


class TooManyMelonsError(ValueError):

    #def __init__(self, msg):
        #self.msg = msg

    def __str__(self):
        return repr(self.message)


class AbstractMelonOrder(TooManyMelonsError, object):
    """Super class for all melon types"""

    # tax = 0.10

    def __init__(self, species, qty, melon_type='secret', country_code=None):
        self.species = species
        self.qty = qty

        self.melon_count(qty)

        self.shipped = False
        self.type = melon_type
        self.country_code = country_code

    def get_base_price(self):
        hour = time.localtime().tm_hour
        day = time.localtime().tm_wday
        base_price = random.randint(5, 9)

        if (hour >= 8 and hour <= 11) and (day < 5):
            return base_price + 4
        return base_price

    def get_total(self):
        """Calculate price."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price
        return round(total, 2)

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

    def melon_count(self, qty):
        if qty > 100:
            raise TooManyMelonsError("No more then 100 melons!")


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic")
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international", country_code)
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def get_total(self):

        if self.qty < 10:
            return 3 + super(InternationalMelonOrder, self).get_total()
        return super(InternationalMelonOrder, self).get_total()


class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed

