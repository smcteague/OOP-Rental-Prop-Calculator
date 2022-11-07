class CashOnCashROI():
    def __init__(self) -> None:
        self.down_payment = None
        self.closing_costs = None
        self.rehab_budget = None
        self.misc_other_costs = None
    
    def get_down_payment(self):
        while not isinstance(self.down_payment, float):
            try:
                if self.down_payment == None:
                    self.down_payment = input("\nWhat is the estimated down payment for this property? ")
                    self.down_payment = float(self.down_payment)
                    break
                else:
                    print("\nPlease enter a number only.")
                    self.down_payment = float(input("What is the estimated down payment for this property? "))
            except:
                print("\nPlease enter a number only.")
                self.down_payment = float(input("What is the estimated down payment for this property? "))
            finally:
                continue

    def get_closing_costs(self):
        while not isinstance(self.closing_costs, float):
            try:
                if self.closing_costs == None:
                    self.closing_costs = input("\nWhat are the estimated total closing costs for this property? ")
                    self.closing_costs = float(self.closing_costs)
                    break
                else:
                    print("\nPlease enter a number only.")
                    self.closing_costs = float(input("What are the estimated total closing costs for this property? "))
            except:
                print("\nPlease enter a number only.")
                self.closing_costs = float(input("What are the estimated total closing costs for this property? "))
            finally:
                continue

    def get_rehab_budget(self):
        while not isinstance(self.rehab_budget, float):
            try:
                if self.rehab_budget == None:
                    self.rehab_budget = input("\nWhat is the estimated rehab budget for this property? ")
                    self.rehab_budget = float(self.rehab_budget)
                    break
                else:
                    print("\nPlease enter a number only.")
                    self.rehab_budget = float(input("What is the estimated rehab budget for this property? "))
            except:
                print("\nPlease enter a number only.")
                self.rehab_budget = float(input("What is the estimated rehab budget for this property? "))
            finally:
                continue

    def get_misc_other_costs(self):
        while not isinstance(self.misc_other_costs, float):
            try:
                if self.misc_other_costs == None:
                    self.misc_other_costs = input("\nWhat are the estimated total miscellaneous other costs for this property? ")
                    self.misc_other_costs = float(self.misc_other_costs)
                    break
                else:
                    print("\nPlease enter a number only.")
                    self.misc_other_costs = float(input("What are the estimated total miscellaneous other costs for this property? "))
            except:
                print("\nPlease enter a number only.")
                self.misc_other_costs = float(input("What are the estimated total miscellaneous other costs for this property? "))
            finally:
                continue