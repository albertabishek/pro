from flask import  render_template,request,send_from_directory,Blueprint
from New_Creation.models import  Haircut_Ratings, Haircut_Shops
from ..models import db
import os

Haircut_details = Blueprint('Haircut_details',__name__,static_folder="static",template_folder="templates")

 

 




#For Haircut Shops


# rendering pages for filling the form

@Haircut_details.route('/Haircut_shop_adding_page')
def Haircut_shop_adding_page():
    return render_template('Haircuts/Haircut_shop_adding_page.html')


# rendering landing pages


@Haircut_details.route('/Haircut_shop_template')
def Haircut_shop_template():
    return render_template('Haircuts/Haircut_shop_template.html')
    

@Haircut_details.route('/Haircut_shop_page',methods=['POST'])
def Haircut_shop_page():
    HaircutD = Haircut_Shops.query.order_by(Haircut_Shops.Shop_name).all()
    if request.method == 'POST':
       Place = request.form['PL1']
       District = request.form['DI1']
       if  HaircutD  and Place and District:
         return render_template('Haircuts/Haircut_shop_page.html',HaircutD=HaircutD, Place=Place,District=District)
       elif  HaircutD  and Place:
         return render_template('Haircuts/Haircut_shop_page.html',HaircutD=HaircutD, Place=Place)
       
    return 'Something went wrong. Please try again.'


# functions to recieve data from forms and store in database

@Haircut_details.route('/Haircut_ratings',methods=['POST'])
def Haircut_rating_data():
    if request.method == 'POST':
        rate = request.form['Rating']
        sname = request.form['sname']
        if rate and sname:
            new_file = Haircut_Ratings(rating=rate,details=sname)
            db.session.add(new_file)
            db.session.commit()
            return render_template('Haircuts/Haircut_rating_success.html')
        
    return 'Something went wrong. Please try  again.'



@Haircut_details.route('/Haircut_shop_upload_page',methods=['POST'])
def Haircut_shop_upload_page():
    if request.method == 'POST':
        file = request.files['file']
        shopname = request.form['shop_name']  # Retrieve the name from the form
        tag2 = request.form['T2']
        tag3 = request.form['T3']
        contact_info = request.form['C_info']
        Llink = request.form['location_link']
        Lname = request.form['location_name']
        quality = request.form['quality']
        

        if file and shopname and Llink  and Lname  and tag2 and tag3 and contact_info :
            filename = file.filename
            file.save(os.path.join('New_Creation/Haircut_images', filename))
            
            # Create a new record in the database with both name and filename
            new_file = Haircut_Shops(Shop_name = shopname , Quality=quality, location_text=Lname, location_link=Llink, filename=filename , P_tag=tag2, D_tag=tag3, contact_Info=contact_info)
            db.session.add(new_file)
            db.session.commit()
            
            return render_template('Haircuts/Haircut_shop_adding_page.html')
    
    return 'Something went wrong. Please try again.'



@Haircut_details.route('/H_uploaded_file/<filename>')
def H_uploaded_file(filename):
    return send_from_directory('Haircut_images', filename)




