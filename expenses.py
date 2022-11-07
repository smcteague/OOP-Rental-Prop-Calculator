class Expenses:
    def __init__(self) -> None:
        self.expenses = {}
        self.total_expenses = None

    def get_expenses(self):
        while True:
            expense_name = input("\nWhat is a source of estimated monthly expense for this property? (or 'quit' or 'q' when done or to exit this question) ")
            expense_name = expense_name.strip().lower()

            if len(expense_name) == 0:
                expense_name = "error"

            if expense_name not in ('quit', 'q'):
                self.expenses[expense_name] = None
                while not isinstance(self.expenses[expense_name], float):
                    try:
                        if self.expenses[expense_name] == None:
                            self.expenses[expense_name] = input(f"\nWhat is the estimated monthly {expense_name} expense for this property? ")
                            self.expenses[expense_name] = float(self.expenses[expense_name])
                        else:
                            print("Please enter a number only.")
                            self.expenses[expense_name] = float(input(f"\nWhat is the estimated monthly {expense_name} expense for this property? "))
                    except:
                        print("Please enter a number only.")
                        self.expenses[expense_name] = float(input(f"\nWhat is the estimated monthly {expense_name} expense for this property? "))
                    finally:
                        continue
            else:
                break

    def edit_expenses(self):
        expense_name = None 
        while expense_name not in ('quit', 'q'):
            expense_name = input("\nWhich source of estimated monthly expense do you want to edit or delete? (or 'quit' or 'q' when done or to exit this question) ")
            expense_name = expense_name.strip().lower()
            while expense_name not in ('quit', 'q') and not self.check_if_expense_exists(expense_name):
                try:
                    print("\nPlease type the name of the expense source correctly.")
                    expense_name = input("Which source of estimated monthly expense do you want to edit or delete? (or 'quit' or 'q' when done or to exit this question) ")
                    expense_name = expense_name.strip().lower()
                except:
                    print("\nPlease type the name of the expense source correctly.")
                    expense_name = input("Which source of estimated monthly expense do you want to edit or delete? (or 'quit' or 'q' when done or to exit this question) ")
                    expense_name = expense_name.strip().lower()
                finally:
                    continue

            menu_option = None
            while menu_option != '4' and expense_name not in ('quit', 'q'):
                print("\n")
                print("-"*30)
                print(f"Options for {expense_name.title()}:")
                print("-"*30)
                print("[1] Edit name")
                print("[2] Edit dollar amount")
                print("[3] Delete entirely")
                print("[4] Done for this expense source")
                print("-"*30)

                menu_option = input("\nPlease enter an option from the menu above: ")
                menu_option = menu_option.strip().lower()

                if menu_option in ('1', '2', '3', '4'):
                    if menu_option == '1':
                        expense_name_edited = input("\nWhat is the edited name for this source of estimated monthly expense? (or 'quit' or 'q' to return to options menu) ")
                        expense_name_edited = expense_name_edited.strip().lower()
                        if expense_name_edited not in ('quit', 'q'):
                            self.expenses[expense_name_edited] = self.expenses[expense_name]
                            del self.expenses[expense_name]

                    if menu_option == '2': 
                        self.expenses[expense_name] = None
                        while not isinstance(self.expenses[expense_name], float):
                            try:
                                if self.expenses[expense_name] == None:
                                    self.expenses[expense_name] = input(f"\nWhat is the estimated monthly {expense_name} expense for this property? ")
                                    self.expenses[expense_name] = float(self.expenses[expense_name])
                                else:
                                    print("\nPlease enter a number only.")
                                    self.expenses[expense_name] = float(input(f"What is the estimated monthly {expense_name} expense for this property? "))
                            except:
                                print("\nPlease enter a number only.")
                                self.expenses[expense_name] = float(input(f"What is the estimated monthly {expense_name} expense for this property? "))
                            finally:
                                continue

                    if menu_option == '3':
                        confirm_delete = input(f"Confirm deletion of the {expense_name} expense source? 'yes' or 'no' ")
                        if confirm_delete in ('yes', 'y'):
                            print(f"{expense_name} was deleted.")
                            del self.expenses[expense_name]
                        else:
                            print(f"{expense_name} was not deleted.")
            else:
                return

    def calculate_total_expenses(self):
        total_expenses = 0.0
        if len(self.expenses) > 0:
            for v in self.expenses.values():
                print(v)
                total_expenses += v
        self.total_expenses = total_expenses
    
    def display_expenses(self):
        if self.total_expenses == None:
            return
        else:
            print("\n")
            print("="*60)
            print("Estimated Monthly Expenses:")
            print("="*60)
            if len(self.expenses) > 0:
                for k, v in self.expenses.items():
                    expense_currency_string = "${:,.2f}".format(v)
                    print(f"{k.title()}: {expense_currency_string}")
            total_expense_currency_string = "${:,.2f}".format(self.total_expenses)
            print("-"*60)
            print(f"Total: {total_expense_currency_string}")
            print("="*60)
            print("\n")

    def check_expenses(self):
        if len(self.expenses) == 0:
            print("\nPlease enter estimated monthly expense before selecting this option.")
            return False
        else:
            return True

    def check_if_expense_exists(self, expense_name):
        try:
            if self.expenses[expense_name]:
                return True
        except:
            return False