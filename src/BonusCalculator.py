class SalesPerson:

    def __init__(self, sales=0, quota=0, commission_percentage=0, tax_percentage=0):
        self.sales = sales
        self.quota = quota
        self.commission_percentage = commission_percentage
        self.tax_percentage = tax_percentage

    def calculate_bonus(self):
        if self.sales>self.quota:
            return (self.sales-self.quota)*self.commission_percentage/100*(100-self.tax_percentage)/100
        return 0

