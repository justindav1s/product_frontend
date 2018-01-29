from flask import render_template, flash, redirect
import urllib3
import json
from app import app
from .forms import ProductForm
from .model import Product

http = urllib3.PoolManager()

@app.route('/', methods=['GET'])
def health():
    return render_template("health.html")

@app.route('/inventory', methods=['GET', 'POST'])
def index():

    form = ProductForm()

    inventory = []

    url = 'http://product-backend:8080/product/'
    print("READ URL : ", url)
    r = http.request('GET', url)
    print(r.data)

    parsed_json = json.loads(r.data.decode("utf-8"))
    for element in parsed_json:
        print(element)
        prod = Product(element['id'], element['name'])
        prod.toString()
        inventory.append(prod)

    if form.validate_on_submit():
        inventory = []
        flash('Product id=%s' %(form.id.data))
        flash('Product name=%s' % (form.name.data))
        createurl = url+"create/"+form.id.data+"/"+form.name.data
        print("CREATE URL : ", createurl)
        r = http.request('POST', createurl)

        parsed_json = json.loads(r.data.decode("utf-8"))
        for element in parsed_json:
            print(element)
            prod = Product(element['id'], element['name'])
            prod.toString()
            inventory.append(prod)

        return redirect('/inventory')
    return render_template("index.html",
                           title='Inventory Manager',
                           form=form,
                           inventory=inventory)