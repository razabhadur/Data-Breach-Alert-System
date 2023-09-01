import requests

class DataBreachAlertSystem:

    def __init__(self):
        self.breach_db = {
            'user1@example.com': [{'breach': 'CompanyA', 'data': 'passwords, emails', 'date': '2022-01-01'}],
            'user2@example.com': [{'breach': 'CompanyB', 'data': 'credit card details', 'date': '2022-02-15'}]
        }
        self.subscribed_emails = set()

    def check_email(self, email):
        return self.breach_db.get(email, [])

    def subscribe_email(self, email):
        self.subscribed_emails.add(email)

    def generate_report(self, breaches):
        report = 'Data Breach Alert Report\n'
        report += '=' * 30 + '\n'
        for breach in breaches:
            report += f'Breach: {breach['breach']}, Data Compromised: {breach['data']}, Date: {breach['date']}\n'
        report += '\nRecommendation: Change your passwords, enable 2FA, and monitor your accounts for suspicious activity.'
        return report

    def run(self):
        email = input('Enter your email address: ')
        breaches = self.check_email(email)
        report = self.generate_report(breaches)
        print(report)
        subscribe_choice = input('Would you like to subscribe for future breach notifications? (yes/no) ')
        if subscribe_choice.lower() == 'yes':
            self.subscribe_email(email)
            print('You have been subscribed for future breach notifications.')

if __name__ == '__main__':
    alert_system = DataBreachAlertSystem()
    alert_system.run()
