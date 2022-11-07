from calculator import Calculator

class Main:
    def displayGreeting():
        print("\nWelcome to Bigger Pockets' Property Rental Income ROI Calculator!\n")

    def displayMainMenu():
        print("\n")
        print("-"*30)
        print("Main Menu Options:")
        print("-"*30)
        print("[1] Input estimated monthly rental income")
        print("[2] Edit estimated monthly rental income")
        print("[3] Input other estimated monthly income")
        print("[4] Edit other estimated monthly income")
        print("[5] Display estimated monthly income")
        print("[6] Input estimated monthly expenses")
        print("[7] Edit estimated monthly expenses")
        print("[8] Display estimated monthly expenses")
        print("[9] Display estimated monthly cash flow")
        print("[10] Input estimated cash-on-cash ROI costs")
        print("[11] Display cash-on-cash ROI")        
        print("[12] Quit")
        print("-"*30)

    def run():
        Main.displayGreeting()
        Main.displayMainMenu()
        new_calculator = Calculator()

        menu_option = None
        while menu_option != '12':
            menu_option = input("\nPlease enter an option from the menu above: ")
            menu_option = menu_option.strip().lower()
            if menu_option == '1':
                new_calculator.get_rental_income()
                new_calculator.calculate_total_income()
                new_calculator.display_income()
                Main.displayMainMenu()
            if menu_option == '2':
                if new_calculator.check_rental_income():
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                    new_calculator.edit_rental_income()
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                Main.displayMainMenu()
            if menu_option == '3':
                if new_calculator.check_rental_income():
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                    new_calculator.get_other_income()
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                Main.displayMainMenu()
            if menu_option == '4':
                if new_calculator.check_other_income():
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                    new_calculator.edit_other_income()
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                Main.displayMainMenu()
            if menu_option == '5':
                if new_calculator.check_rental_income():
                    new_calculator.calculate_total_income()
                    new_calculator.display_income()
                Main.displayMainMenu()
            if menu_option == '6':
                new_calculator.get_expenses()
                new_calculator.calculate_total_expenses()
                new_calculator.display_expenses()
                Main.displayMainMenu()
            if menu_option == '7':
                if new_calculator.check_expenses():
                    new_calculator.calculate_total_expenses()
                    new_calculator.display_expenses()
                    new_calculator.edit_expenses()
                    new_calculator.calculate_total_expenses()
                    new_calculator.display_expenses()                    
                Main.displayMainMenu()
            if menu_option == '8':
                if new_calculator.check_expenses():
                    new_calculator.calculate_total_expenses()
                    new_calculator.display_expenses()
                Main.displayMainMenu()
            if menu_option == '9':
                new_calculator.calculate_cash_flow()
                if new_calculator.check_cash_flow():
                    new_calculator.display_cashflow()
                Main.displayMainMenu()
            if menu_option == '10':
                new_calculator.calculate_cash_flow()
                if new_calculator.check_cash_flow():
                    new_calculator.get_down_payment()
                    new_calculator.get_closing_costs()
                    new_calculator.get_rehab_budget()
                    new_calculator.get_misc_other_costs()
                    new_calculator.calculate_cash_on_cash_roi()
                    new_calculator.display_cash_on_cash_roi()
                Main.displayMainMenu()
            if menu_option == '11':
                new_calculator.calculate_cash_on_cash_roi()
                if new_calculator.check_cash_on_cash_roi:
                    new_calculator.calculate_cash_on_cash_roi()
                    new_calculator.display_cash_on_cash_roi()
                Main.displayMainMenu()

        print("\nThank you for using our calculator. Please come again!\n")

Main.run()
