from run import app
import os,sys
from flask import render_template,redirect,request
from werkzeug.utils import secure_filename

@app.route('/admin/products',methods=['GET','POST'])
def admin_products():
    from run import db
    from models import Products
    products=Products.query.all()

    if request.method=='POST':
        file=request.files['product_img']
        filename=file.filename
        title=secure_filename(request.form['product_name'])
        file_extention=filename.split(".")[-1]
        filename=title+'.'+file_extention
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        product=Products(
            product_sale=request.form['product_sale'],
            product_sale_name=request.form['product_sale_name'],
            product_category=request.form['product_category'],
            product_sub_category=request.form['product_sub_category'],
            product_name=request.form['product_name'],
            product_price=request.form['product_price'],
            product_img=filename,
            product_simple_description=request.form['product_simple_description'],
            product_details_description=request.form['product_details_description'],
            product_old_price=request.form['product_old_price']
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/admin/products')
    return render_template('admin/products.html',products=products)

@app.route('/admin/products/delete/<id>')
def delete_product(id):
    from models import Products
    from run import db
    user=Products.query.get(id)
    db.session.delete(user)
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'],user.product_img))
    db.session.commit()
    return redirect('/admin/products')