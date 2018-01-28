from flask import render_template, flash, redirect
import urllib3
import json
from app import app
from .forms import ProductForm
from .model import Product

inventory = []
http = urllib3.PoolManager()

@app.route('/inventory', methods=['GET', 'POST'])
def index():

    form = ProductForm()

    inventory = []

    #r = http.request('GET', 'http://productsrv:8080/product/')

    url = 'http://product-backend/product/'
    print("URL : ", url)

    r = http.request('GET', url)
    #r = http.request('GET', 'http://productv3-prod-services.172.16.173.128.nip.io/product/')
    print(r.data)

    parsed_json = json.loads(r.data.decode("utf-8"))
    for element in parsed_json:
        print(element)
        prod = Product(element['id'], element['name'])
        prod.toString()
        inventory.append(prod)

    if form.validate_on_submit():

        flash('Product id=%s' %(form.id.data))
        flash('Product name=%s' % (form.name.data))
        prod = Product(form.id.data, form.name.data)
        inventory.append(prod)
        return redirect('/inventory')
    return render_template("index.html",
                           title='Inventory Manager',
                           form=form,
                           inventory=inventory)