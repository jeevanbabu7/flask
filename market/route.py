from flask import render_template,redirect,url_for,flash,get_flashed_messages,request
from market import app,db
from market.models import User,CartItem,Item,AddressItem
from market.forms import RegisterForm,LoginForm
from flask_login import login_user,logout_user,login_required,UserMixin,current_user
from flask_mail import Mail,Message
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

mail = Mail(app)
msgdemo = 'Hii , Welcome to kpMart'
#-----------------------------Home page --------------------------------------------

@app.route("/home")
@app.route("/")
@login_required
def home_page():
    return render_template('home.html')

#-----------------------Home ends----------------------


#---------------------market-------------------------------

@app.route("/market")
@login_required   #it will take the user to the login page if the user is not logged in
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

#----------------market end---------------------------------------------------------------------------------------------

@app.route("/register" , methods = ['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_create = User(username = form.username.data,
                           email_address = form.email_address.data , 
                           password = form.password1.data)
        db.session.add(user_create)
        db.session.commit()
        # if request.method=='POST':
        #     msg = Message('Hii',sender='jeevanbabu190@gmail.com',recipients=['jeevanbabu190@gmail.com'])
        #     msg.body = msgdemo
        #     mail.send(msg)
        login_user(user_create)
        flash(f' You are logged in as {user_create.username}',category = 'success')
        return redirect(url_for('market_page'))
    if form.errors !={} : #if there are no errors
        for error_msg in form.errors.values():
            flash(f' There was an error {error_msg}',category = 'danger')
    return render_template('register.html',form = form)

#------------------------------------Profile------------------------------------

@app.route("/profile/<username>")
def profile_page(username):
    with app.app_context():
        cart = CartItem.query.filter_by(username= username)
    return render_template('profile.html',cart = cart)

#----------------------------profile end----------------------------
@app.route("/address",methods=["GET","POST"])
def address():
    itemname = request.form['nameofitem']
    return render_template("address.html")



@app.route('/login', methods =['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()  # get returns a single value , no need for first()
        if user and user.check_password_correction(
            user_password = form.password.data
            ):
 
            login_user(user)
            flash(f'Succes! You are logged in as {user.username}',category = 'success')
            return redirect(url_for('market_page'))
        else:
            flash(f'Username and password are not matching , try again ; )',category = 'danger')

    return render_template('login.html',form =form)


@app.route('/logout',methods = ['GET','POST'])
def logout_page():
    logout_user()
    flash('Successfully  logged out',category = 'info')
    return redirect(url_for('login_page'))


@app.route("/cart",methods=["GET","POST"])
def go_cart():
    items = CartItem.query.filter_by(username = current_user.username).all()
    return render_template('mycart.html',items = items)

@app.route('/process_form', methods=['POST'])
def process_form():
    username = request.form['username']
    itemname = request.form['nameofitem']
    street = request.form['street']
    landmark = request.form['landmark']
    city = request.form['city']
    state = request.form['state']
    pincode = request.form['pincode']
    mobile = request.form['mobile']

    with app.app_context():
        newaddress=AddressItem(username=current_user.username,itemname=itemname ,street=street,landmark=landmark,city=city,state=state,pincode=pincode,mobilenumber=mobile)
        db.session.add(newaddress)
        db.session.commit()

    return render_template("market.html")


@app.route("/add_to_cart" ,methods = ["POST"])
def add_to_cart():
    user_name =  request.form['username']
    item_name = request.form['itemname']
    item_price = request.form['itemprice']
    count  = request.form['itemcount']
    item_pic=request.form['itempic']
    existing_item = CartItem.query.filter(CartItem.username==user_name , CartItem.itemname==item_name).first()
    if existing_item:
        flash('Item already in cart',category="success")
       
    else:
         with app.app_context():
            #newcount=Item.query.filter_by()
            #engine = create_engine('sqlite:///market.db')


            #Session = sessionmaker(bind=engine)
           #newcount = Session()
            #newcount = newcount.query(Item).filter_by(name =item_name).first()
            

      
            #newcount.commit()

            new_item = CartItem(username=user_name, itemname=item_name,itemprice=item_price,itemcount = count,itempic=item_pic)
            db.session.add(new_item)
            db.session.commit()
            flash("Successfully added to your cart",category="success")
        
   
    
    return redirect(url_for('market_page'))