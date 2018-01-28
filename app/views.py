from flask import render_template, flash, redirect
import urllib3
import json
from app import app
from .forms import ProductForm
from .model import Product

inventory = []
http = urllib3.PoolManager()

@app.route('/products', methods=['GET', 'POST'])
def index():
    form = ProductForm()
    r = http.request('GET', 'http://product/product/1')
    print(r.data)
    parsed_json = json.loads(r.data.decode("utf-8"))
    prod = Product(parsed_json['id'], parsed_json['name'])
    prod.toString()
    inventory.append(prod)

    if form.validate_on_submit():

        flash('Product id=%s' %(form.id.data))
        flash('Product name=%s' % (form.name.data))
        prod = Product(form.id.data, form.name.data)
        inventory.append(prod)
        return redirect('/products')
    return render_template("index.html",
                           title='Inventory Manager',
                           form=form,
                           inventory=inventory)