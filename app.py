# Import libraries
from flask import Flask, request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions()
    return render_template("transactions.html", transactions = transactions)

# Create operation

@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    try:
        transaction = next((trans for trans in transactions if trans['id'] == transaction_id ))
    except:
        transaction = None
    
    if request.method == 'POST':
        try:
            next_id = max(data, key=lambda x: x['id'])['id']+1
        except:
            next_id =0

        transaction = {
            'id':       next_id + 1,
            'date':     request.form.get('date'),
            'amount':   request.form.get('amount')           
        }

        transactions.append(transaction)
        return redirect(url_for("get_transactions"))

    return redirect("form.html")
# Update operation
@app.route("/edit/<int:transaction_id>",methods : ["GET", "POST"])
def edit_transaction(transaction_id):
    try:
        transaction = next((trans for trans in transactions if trans['id'] == transaction_id ))
    except:
        transaction = None
        
    if transaction and request.method == "POST":
        transaction['date'] = request.form['date']
        transaction['amount'] = request.form['amount']
    
        return redirect(url_for("get_transactions"))
    elif transaction:
        return render_template("edit.html", transaction=transaction)
    
    return ({"message": "This transaction id is not found"}, 404)
# Delete operation
@app.route("/delete/<int: transaction_id")
def delete_transaction(transaction_id):
    try:
        transaction = next((trans for trans in transactions if trans['id'] == transaction_id ))
    except:
        transaction = None

    if transaction:
        transactions.remove(transaction)
        

    return redirect(url_for("get_transactions"))  

# Run the Flask app
    

if __name__ == "__main__":
    app.run(degug, True)