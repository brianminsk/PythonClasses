import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donor, Donation, db

from peewee import DoesNotExist

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/new/', methods=['GET', 'POST'])
def new_donation():
    if request.method == 'POST':
        donor_name = request.form["name"]
        amount = request.form["amount"]
        print(donor_name, amount)

        with db:
            try:
                donor = Donor.get(Donor.name == donor_name)
            except DoesNotExist:
                donor = Donor(name=donor_name)
                donor.save()

            Donation(value=amount, donor=donor).save()

        return redirect(url_for('all'))
    else:
        return render_template('new.jinja2')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
