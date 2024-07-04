from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import Shoe, Shoe_Ratings, Shoe_Shops
from ..models import db
import os

Shoe_details = Blueprint('Shoe_details',__name__,static_folder="static",template_folder="templates")

 

 




#For Shoe Shops


# rendering pages for filling the form

@Shoe_details.route('/shoe_adding_page')
def shoe_adding_page():
    return render_template('Shoes/shoe_adding_page.html')


@Shoe_details.route('/shoe_shop_adding_page')
def shoe_shop_adding_page():
    return render_template('Shoes/shoe_shop_adding_page.html')


# rendering landing pages

@Shoe_details.route('/shoe_template')
def shoe_template():
    return render_template('Shoes/shoe_template.html')

@Shoe_details.route('/shoes_page',methods=['POST'])
def shoes_page():
    shoes = Shoe.query.order_by(Shoe.name).all()
    if request.method == 'POST':
        C1 = request.form['C1']
        if C1 :
           return render_template('Shoes/shoes_page.html',shoes=shoes,C1=C1)
    return 'Something went wrong. Please try again.'



@Shoe_details.route('/shoe_shop_template',methods=['POST'])
def shoe_shop_template():
    if request.method == 'POST':
        Slink = request.form['Shoe_name']
        if Slink:
           return render_template('Shoes/shoe_shop_template.html',Slink=Slink)
    return 'Something went wrong. Please try again.'

@Shoe_details.route('/shoe_shop_page',methods=['POST'])
def shoe_shop_page():
    shopies = Shoe_Shops.query.order_by(Shoe_Shops.Shop_name).all()
    if request.method == 'POST':
       Slink = request.form['Slink']
       Price = request.form['PR1']
       Place = request.form['PL1']
       District = request.form['DI1']
       if Slink and shopies and Price and Place and District:
         return render_template('Shoes/shoe_shop_page.html',shopies=shopies,Slink=Slink,Price=int(Price),Place=Place,District=District)
       elif Slink and shopies and Price and Place:
         return render_template('Shoes/shoe_shop_page.html',shopies=shopies,Slink=Slink,Price=int(Price),Place=Place)

    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@Shoe_details.route('/shoe_ratings',methods=['POST'])
def shoe_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = Shoe_Ratings(rating=rate,details=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('Shoes/shoe_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@Shoe_details.route('/shoe_shop_upload_page',methods=['POST'])
def shoe_shop_upload_page():
    if request.method == 'POST':
        file = request.files['file']
        shopname = request.form['shop_name']  # Retrieve the name from the form
        tag1 = request.form['T1']
        tag2 = request.form['T2']
        tag3 = request.form['T3']
        contact_info = request.form['C_info']
        Llink = request.form['location_link']
        Lname = request.form['location_name']
        quality = request.form['quality']
        price = request.form['price']

        if file and shopname and Llink and price and Lname  and tag1 and tag2 and tag3 and contact_info :
            filename = file.filename
            file.save(os.path.join('New_Creation/Shoes_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = Shoe_Shops(Shop_name = shopname , price = price, Quality=quality, location_text=Lname, location_link=Llink, filename=filename, S_tag=tag1, P_tag=tag2, D_tag=tag3, contact_Info=contact_info)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('Shoes/shoe_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@Shoe_details.route('/shoe_upload_page',methods=['POST'])
def shoe_upload_page():
    if request.method == 'POST':
        name = request.form['name1']  # Retrieve the name from the form
        Category1 = request.form['C1']
        link = request.form['links']
        file = request.files['file']
       
        if file and name and link and Category1 :
            filename = file.filename
            file.save(os.path.join('New_Creation/Shoes_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = Shoe(name=name, link=link, filename=filename, category_1=Category1 )
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('Shoes/shoe_adding_page.html')
    
    return 'Something went wrong. Please try again.'


@Shoe_details.route('/S_uploaded_file/<filename>')
def S_uploaded_file(filename):
    return send_from_directory('Shoes_images', filename)




