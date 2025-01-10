from flask import render_template, redirect, request
from flask_login import login_user, logout_user, current_user, login_required
from os import path
from uuid import uuid4

from forms import ProductForm, RegisterForm, LoginForm, ItemForm, ProForm
from models import Product, User, Item, Pro
from ext import app, db



@app.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@app.route("/chvenshesaxeb")
def chvenshesaxeb():
    return render_template("ჩვენ შესახებ.html")


@app.route("/sakontaqto")
def sakontaqto():
    return render_template("საკონტაქტო.html")


@app.route("/animatorebi")
def animatorebi():
    products = Product.query.all()
    return render_template("ანიმატორები.html", products=products)


@app.route("/gmirebi")
def gmirebi():
    items = Item.query.all()
    return render_template("გმირები.html", items=items)


@app.route("/programebi")
def programebi():
    pros = Pro.query.all()
    return render_template("პროგრამები.html", pros=pros)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data,
                        role="Guest")
        new_user.create()
        return redirect("/login")
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user != None and user.password == form.password.data:
            login_user(user)
            return redirect("/")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")



@app.route("/create_product", methods=["GET", "POST"])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():




        new_product = Product(name=form.name.data,
                              text=form.text.data,
                              img=form.img.data)
        db.session.add(new_product)
        db.session.commit()
        return redirect("/animatorebi")
    return render_template("create_product.html", form=form)

@app.route("/create_item", methods=["GET", "POST"])
@login_required
def create_item():
    form = ProductForm()
    if form.validate_on_submit():



        new_item = Item(name=form.name.data,
                              text=form.text.data,
                              img=form.img.data)
        db.session.add(new_item)
        db.session.commit()
        return redirect("/gmirebi")
    return render_template("create_item.html", form=form)

@app.route("/create_pro", methods=["GET", "POST"])
@login_required
def create_pro():
    form = ProForm()
    if form.validate_on_submit():


        new_pro = Pro(name=form.name.data,
                              text=form.text.data,
                              img=form.img.data)
        db.session.add(new_pro)
        db.session.commit()
        return redirect("/programebi")
    return render_template("create_pro.html", form=form)

@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):

    product = Product.query.get(product_id)
    form = ProductForm(name=product.name, text=product.text, img=product.img)
    if form.validate_on_submit():
        product.name = form.name.data
        product.text = form.text.data
        product.img = form.img.data
        db.session.commit()
        return redirect("/animatorebi")
    return render_template("create_product.html", form=form)

@app.route("/delete_product/<int:product_id>", methods=["GET", "POST"])
def delete_product(product_id):
    product= Product.query.get(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect("/animatorebi")

@app.route("/edit_item/<int:item_id>", methods=["GET", "POST"])
def edit_item(item_id):

    item = Item.query.get(item_id)
    form = ItemForm(name=item.name, text=item.text, img=item.img)
    if form.validate_on_submit():
        item.name = form.name.data
        item.text = form.text.data
        item.img = form.img.data
        db.session.commit()
        return redirect("/gmirebi")
    return render_template("create_item.html", form=form)

@app.route("/delete_item/<int:item_id>", methods=["GET", "POST"])
def delete_item(item_id):
    item= Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect("/gmirebi")

@app.route("/edit_pro/<int:pro_id>", methods=["GET", "POST"])
def edit_pro(pro_id):

    pro = Pro.query.get(pro_id)
    form = ProForm(name=pro.name, text=pro.text, img=pro.img)
    if form.validate_on_submit():
        pro.name = form.name.data
        pro.text = form.text.data
        pro.img = form.img.data
        db.session.commit()
        return redirect("/programebi")
    return render_template("create_pro.html", form=form)

@app.route("/delete_pro/<int:pro_id>", methods=["GET", "POST"])
def delete_pro(pro_id):
    pro= Pro.query.get(pro_id)
    db.session.delete(pro)
    db.session.commit()
    return redirect("/programebi")
