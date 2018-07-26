import webapp2
import jinja2
import os
from transaction import Transaction
import time

jinja_loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
jinja_current_directory = jinja2.Environment(
    loader = jinja_loader,
    extensions = ['jinja2.ext.autoescape'],
    autoescape=True)


def get_balance():
    # get all transactions in our account
    transactions = Transaction.query().fetch()

    balance = 0
    for trans in transactions:
        balance += trans.amount
    return balance

class BankingHandler(webapp2.RequestHandler):
    def get(self):
        bank_template = jinja_current_directory.get_template('templates/index.html')
        my_dict = {'current_balance': get_balance()}
        self.response.write(bank_template.render(my_dict))

class MoneyHandler(webapp2.RequestHandler):
    def post(self):
        bank_template = jinja_current_directory.get_template('templates/index.html')
        transaction = Transaction(amount = int(self.request.get('amount')))
        transaction.put()
        time.sleep(1)
        my_dict = {'current_balance': get_balance()}
        self.response.write(bank_template.render(my_dict))


        # Transaction.query().fetch()
        #
        # # get all transactions in our account
        # transactions = Transaction.query().fetch()
        # add up the Balance
# def get_balance():
#     balance = 0
#     for trans in transactions:
#         balance = trans.amount
#     return balance


        # amount = Int(self.request.get('amount'))
        # balance = balance + int(self.request.get('amount'))
        # my_dict = {'current_balance': balance}
        # self.response.write(bank_template.render(my_dict))
        # my_dict.put()



app = webapp2.WSGIApplication([
('/banking', BankingHandler),
('/money', MoneyHandler),
], debug=True)
