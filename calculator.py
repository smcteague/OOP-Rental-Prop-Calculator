from income import Income
from expenses import Expenses
from cash_on_cash_roi_costs import CashOnCashROI

class Calculator(Income, Expenses, CashOnCashROI):
    def __init__(self) -> None:
        Income.__init__(self)
        Expenses.__init__(self)
        self.cash_flow = None
        self.down_payment = None
        self.closing_costs = None
        self.rehab_budget = None
        self.misc_other_costs = None
        self.total_investment = None
        self.annual_cash_flow = None
        self.cash_on_cash_roi = None

    def calculate_cash_flow(self):
        if self.total_income != None and self.total_expenses != None:
            self.cash_flow = self.total_income - self.total_expenses
        else:
            return

    def display_cashflow(self):
        if self.cash_flow == None:
            return
        else:
            print("\n")
            print("="*60)
            print("Estimated Monthly Cash Flow:")
            print("="*60)
            total_income_currency_string = "${:,.2f}".format(self.total_income)
            print(f"Total Income: {total_income_currency_string}")
            total_expenses_currency_string = "${:,.2f}".format(self.total_expenses)
            print(f"Total Expenses: {total_expenses_currency_string}")
            print("-"*60)
            cash_flow_currency_string = "${:,.2f}".format(self.cash_flow)
            print(f"Total Cash Flow: {cash_flow_currency_string}")
            print("="*60)
            print("\n")

    def check_cash_flow(self):
        if self.cash_flow == None:
            print("\nPlease enter estimated monthly income and expenses before choosing this option.")
            return False
        else:
            return True

    def calculate_cash_on_cash_roi(self):
        if self.down_payment != None and self.closing_costs != None \
            and self.rehab_budget != None and self.misc_other_costs != None:
            
            self.total_investment = self.down_payment + self.closing_costs \
            + self.rehab_budget + self.misc_other_costs
            
            self.annual_cash_flow = self.cash_flow * 12
            
            self.cash_on_cash_roi = (self.annual_cash_flow / self.total_investment) * 100
        else:
            print("\nPlease enter estimated monthly income and expenses and cash-on-cash ROI costs before choosing this option.")

    def display_cash_on_cash_roi(self):
        if self.cash_on_cash_roi == None:
            return
        else:
            print("\n")
            print("="*60)
            print("Estimated Cash-On-Cash ROI:")
            print("="*60)
            total_investment_currency_string = "${:,.2f}".format(self.total_investment)
            print(f"Total Investment: {total_investment_currency_string}")
            annual_cash_flow_currency_string = "${:,.2f}".format(self.annual_cash_flow)
            print(f"Annual Cash Flow: {annual_cash_flow_currency_string}")
            print("-"*60)
            cash_on_cash_roi_currency_string = "${:. 0%}".format(self.cash_on_cash_roi)
            print(f"Total Cash Flow: {cash_on_cash_roi_currency_string}")
            print("="*60)
            print("\n")

    def check_cash_on_cash_roi(self):
        if self.cash_on_cash_roi == None:
            return False
        else:
            return True