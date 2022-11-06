class Income():
    def __init__(self) -> None:
        self.rental_income = None
        self.other_income = {}

    def get_rental_income(self):
        while not isinstance(self.rental_income, float):
            try:
                if self.rental_income == None:
                    self.rental_income = input("What is the estimated monthly rental income for this property? ")
                    self.rental_income = float(self.rental_income)
                    break
                else:
                    print("Please enter a number only.")
                    self.rental_income = float(input("What is the estimated monthly rental income for this property? "))
            except:
                print("Please enter a number only.")
                self.rental_income = float(input("What is the estimated monthly rental income for this property? "))
            finally:
                continue

    def get_other_income(self):
        while True:
            other_income_name = input("What is another source of estimated income for this property? (or 'none' or 'quit' when done) ")
            other_income_name = other_income_name.strip().lower()

            if other_income_name not in ('none', 'quit'):
                self.other_income[other_income_name] = None
                while not isinstance(self.other_income[other_income_name], float):
                    try:
                        if self.other_income[other_income_name] == None:
                            self.other_income[other_income_name] = input(f"What is the estimated monthly {other_income_name} income for this property? ")
                            self.other_income[other_income_name] = float(self.other_income[other_income_name])
                        else:
                            print("Please enter a number only.")
                            self.other_income[other_income_name] = float(input(f"What is the estimated monthly {other_income_name} income for this property? "))
                    except:
                        print("Please enter a number only.")
                        self.other_income[other_income_name] = float(input(f"What is the estimated monthly {other_income_name} income for this property? "))
                    finally:
                        continue
            else:
                break
    
    def display_income(self):
        rental_income_currency_string = "${:,.2f}".format(self.rental_income)
        print(f"Estimated Monthly Rental Income: {rental_income_currency_string}")
        if len(self.other_income) > 0:
            for k, v in self.other_income.items():
               v_currency_string = "${:,.2f}".format(v)
               print(f"Estimated Monthly {k.title()} Income: {v_currency_string}")




test = Income()

test.get_rental_income()
test.get_other_income()
test.display_income()

