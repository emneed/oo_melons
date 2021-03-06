"""This file should have our order classes in it."""


class AbstractMelonOrder(object):
    """Super class for all melon types"""

    # tax = 0.10

    def __init__(self, species, qty, melon_type, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.type = melon_type
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


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
