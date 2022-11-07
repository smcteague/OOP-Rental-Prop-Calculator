class Income:
    def __init__(self) -> None:
        self.rental_income = None
        self.other_income = {}
        self.total_income = None

    def get_rental_income(self):
        while not isinstance(self.rental_income, float):
            try:
                if self.rental_income == None:
                    self.rental_income = input("\nWhat is the estimated monthly rental income for this property? ")
                    self.rental_income = float(self.rental_income)
                    break
                else:
                    print("\nPlease enter a number only.")
                    self.rental_income = float(input("What is the estimated monthly rental income for this property? "))
            except:
                print("\nPlease enter a number only.")
                self.rental_income = float(input("What is the estimated monthly rental income for this property? "))
            finally:
                continue
        
    def edit_rental_income(self):
        self.rental_income = None
        self.get_rental_income()

    def get_other_income(self):
        while True:
            other_income_name = input("\nWhat is another source of estimated monthly income for this property? (or 'quit' or 'q' when done or to exit this question) ")
            other_income_name = other_income_name.strip().lower()

            if len(other_income_name) == 0:
                other_income_name = "error"

            if other_income_name not in ('quit', 'q'):
                self.other_income[other_income_name] = None
                while not isinstance(self.other_income[other_income_name], float):
                    try:
                        if self.other_income[other_income_name] == None:
                            self.other_income[other_income_name] = input(f"\nWhat is the estimated monthly {other_income_name} income for this property? ")
                            self.other_income[other_income_name] = float(self.other_income[other_income_name])
                        else:
                            print("Please enter a number only.")
                            self.other_income[other_income_name] = float(input(f"\nWhat is the estimated monthly {other_income_name} income for this property? "))
                    except:
                        print("Please enter a number only.")
                        self.other_income[other_income_name] = float(input(f"\nWhat is the estimated monthly {other_income_name} income for this property? "))
                    finally:
                        continue
            else:
                break

    def edit_other_income(self):
        other_income_name = None 
        while other_income_name not in ('quit', 'q'):
            other_income_name = input("\nWhich source of estimated monthly income do you want to edit or delete? (or 'quit' or 'q' when done or to exit this question) ")
            other_income_name = other_income_name.strip().lower()
            while other_income_name not in ('quit', 'q') and not self.check_if_other_income_exists(other_income_name):
                try:
                    print("\nPlease type the name of the other income source correctly.")
                    other_income_name = input("Which source of estimated monthly income do you want to edit or delete? (or 'quit' or 'q' when done or to exit this question) ")
                    other_income_name = other_income_name.strip().lower()
                except:
                    print("\nPlease type the name of the other income source correctly.")
                    other_income_name = input("Which source of estimated monthly income do you want to edit or delete? (or 'quit' or 'q' when done or to exit this question) ")
                    other_income_name = other_income_name.strip().lower()
                finally:
                    continue

            menu_option = None
            while menu_option != '4' and other_income_name not in ('quit', 'q'):
                print("\n")
                print("-"*30)
                print(f"Options for {other_income_name.title()}:")
                print("-"*30)
                print("[1] Edit name")
                print("[2] Edit dollar amount")
                print("[3] Delete entirely")
                print("[4] Done for this income source")
                print("-"*30)

                menu_option = input("\nPlease enter an option from the menu above: ")
                menu_option = menu_option.strip().lower()

                if menu_option in ('1', '2', '3', '4'):
                    if menu_option == '1':
                        other_income_name_edited = input("\nWhat is the edited name for this source of estimated monthly income? (or 'quit' or 'q' to return to options menu) ")
                        other_income_name_edited = other_income_name_edited.strip().lower()
                        if other_income_name_edited not in ('quit', 'q'):
                            self.other_income[other_income_name_edited] = self.other_income[other_income_name]
                            del self.other_income[other_income_name]

                    if menu_option == '2': 
                        self.other_income[other_income_name] = None
                        while not isinstance(self.other_income[other_income_name], float):
                            try:
                                if self.other_income[other_income_name] == None:
                                    self.other_income[other_income_name] = input(f"\nWhat is the estimated monthly {other_income_name} income for this property? ")
                                    self.other_income[other_income_name] = float(self.other_income[other_income_name])
                                else:
                                    print("\nPlease enter a number only.")
                                    self.other_income[other_income_name] = float(input(f"What is the estimated monthly {other_income_name} income for this property? "))
                            except:
                                print("\nPlease enter a number only.")
                                self.other_income[other_income_name] = float(input(f"What is the estimated monthly {other_income_name} income for this property? "))
                            finally:
                                continue

                    if menu_option == '3':
                        confirm_delete = input(f"Confirm deletion of the {other_income_name} income source? 'yes' or 'no' ")
                        if confirm_delete in ('yes', 'y'):
                            print(f"{other_income_name} was deleted.")
                            del self.other_income[other_income_name]
                        else:
                            print(f"{other_income_name} was not deleted.")
            else:
                return

    def calculate_total_income(self):
        total_other_income = 0.0
        if len(self.other_income) > 0:
            for v in self.other_income.values():
                total_other_income += v
        self.total_income = self.rental_income + total_other_income
    
    def display_income(self):
        if self.total_income == None:
            return
        else:
            print("\n")
            print("="*60)
            print("Estimated Monthly Income:")
            print("="*60)
            rental_income_currency_string = "${:,.2f}".format(self.rental_income)
            print(f"Rent: {rental_income_currency_string}")
            if len(self.other_income) > 0:
                for k, v in self.other_income.items():
                    other_income_currency_string = "${:,.2f}".format(v)
                    print(f"{k.title()}: {other_income_currency_string}")
            total_income_currency_string = "${:,.2f}".format(self.total_income)
            print("-"*60)
            print(f"Total: {total_income_currency_string}")
            print("="*60)
            print("\n")

    def check_rental_income(self):
        if self.rental_income == None:
            print("\nPlease enter estimated monthly rental income before choosing this option.")
            return False
        else:
            return True

    def check_other_income(self):
        if len(self.other_income) == 0:
            if self.rental_income != None:
                print("\nPlease enter other estimated monthly income before selecting this option.")
            else:
                print("\nPlease enter estimated monthly rental income before selecting this option.")
            return False
        else:
            return True

    def check_if_other_income_exists(self, other_income_name):
        try:
            if self.other_income[other_income_name]:
                return True
        except:
            return False