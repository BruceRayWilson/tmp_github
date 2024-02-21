class Accounting:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, date, description):
        self.transactions.append({'amount': amount, 'date': date, 'description': description})

    def get_balance(self):
        return sum(t['amount'] for t in self.transactions)

    def generate_report(self):
        report = "Date\tAmount\tDescription\n"
        for transaction in self.transactions:
            report += f"{transaction['date']}\t{transaction['amount']}\t{transaction['description']}\n"
        return report
