from run import app
from models import Categories
from run import db
import os
from flask import render_template,redirect,request,url_for

@app.route("/admin/categories",methods=["GET","POST"])
def add_and_show_categories():
    all_categories = Categories.query.all()
    if request.method=="POST":
        category_name=request.form["category_name"]
        category=Categories(categories_name=category_name)
        db.session.add(category)
        db.session.commit()
        return redirect('/admin/categories')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template("admin/category.html",categories=all_categories)
    else:
        return redirect(url_for('login'))

@app.route('/admin/categories/delete/<id>')
def delete_category(id):
    user=Categories.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/categories')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
            return render_template("admin/category.html",categories=all_categories)
    else:
        return redirect(url_for('login'))

@app.route("/admin/categories/edit/<id>",methods=["GET","POST"])
def edit_category(id):
    selected_category=Categories.query.get(id)
    all_categories=Categories.query.all()
    if request.method=="POST":
        selected_category.categories_name=request.form["category_name"]
        db.session.commit()
        return redirect('/admin/categories')
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return render_template("admin/category.html",categories=all_categories,selected_category=selected_category)
    else:
        return redirect(url_for('login'))
