import unittest
from BonusCalculator import SalesPerson


# A testcase is created by subclassing unittest.TestCase.
class BonusCalculatorTest(unittest.TestCase):

    def test_init_person_sales(self):
        person = SalesPerson()
        self.assertEqual(person.sales, 0)
        self.assertEqual(person.quota, 0)
        self.assertEqual(person.commission_percentage, 0)
        self.assertEqual(person.tax_percentage, 0)

    def test_set_initial_values_in_sales_person(self):
        person = SalesPerson(sales=12000, quota=15000, commission_percentage = 10, tax_percentage=10)
        self.assertEqual(person.sales, 12000)
        self.assertEqual(person.quota, 15000)
        self.assertEqual(person.commission_percentage, 10)
        self.assertEqual(person.tax_percentage, 10)

    def test_calculate_individual_bonus_when_sales_less_quota(self):
        person = SalesPerson(sales=12000, quota=15000)
        bonus = person.calculate_bonus()
        self.assertEqual(bonus, 0)

    def test_calculate_individual_bonus_when_sales_greater_quota(self):
        person = SalesPerson(sales=12000, quota=11000, commission_percentage=10)
        bonus = person.calculate_bonus()
        self.assertEqual(bonus, 100)

    def test_calculate_individual_bonus_when_sales_greater_quota_and_set_tax(self):
        person = SalesPerson(sales=12000, quota=11000, commission_percentage=10, tax_percentage=10)
        bonus = person.calculate_bonus()
        self.assertEqual(bonus, 90)

    def test_calculate_individual_bonus_when_sales_equal_quota(self):
        person = SalesPerson(sales=12000, quota=12000, commission_percentage=10, tax_percentage=10)
        bonus = person.calculate_bonus()
        self.assertEqual(bonus, 0)


if __name__ == '__main__':
    unittest.main()
