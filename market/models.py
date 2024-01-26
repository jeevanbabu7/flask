from market import db
from market import bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
     id = db.Column(db.Integer(), primary_key=True)
     username = db.Column(db.String(length = 30) , nullable = False,unique = True)
     email_address = db.Column(db.String(length = 30) , nullable = False ,unique = True)
     password_hash = db.Column(db.String(length = 60),nullable = False)
     budget = db.Column(db.Integer(),nullable = False  , default = 1000)
     items = db.relationship('Item',backref = 'owned_user', lazy = True)  #lazy = True should be provided 

    #  @property
    #  def prettier_budget(self):
    #      if(len(str(self.budget))>4):
    #          pass
    #      else return 
     
    
     @property
     def password(self):
         return self.password
     @password.setter
     def password(self,plain_text_pasword):
         self.password_hash = bcrypt.generate_password_hash(plain_text_pasword).decode('utf-8')  #password entered by the user will be taken by the setter an
    
    #-------Password checker------------------------------------------------------------>                                            # hash it
     def check_password_correction(self,user_password):
        return bcrypt.check_password_hash(self.password_hash,user_password)
             
            
class Item(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30))
    barcode = db.Column(db.String(length=30), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=256), nullable=False)
    count=db.Column(db.Integer(),nullable=False,default=10)
    image_url=db.Column(db.String(2000))
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))

    def __repr__(self):

        return f'Item {self.name}'    #It will show the name of the object when querying  
    

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    itemname = db.Column(db.String(100))
    itemprice=db.Column(db.Integer(),nullable=True)
    itemcount=db.Column(db.Integer(),nullable = False)
    itempic=db.Column(db.String(2000))

class AddressItem(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(30),nullable=False)
    itemname=db.Column(db.String(30))
    street=db.Column(db.String(100))
    landmark=db.Column(db.String(100))
    city=db.Column(db.String(50))
    state=db.Column(db.String(50))
    pincode=db.Column(db.String(10))
    mobilenumber=db.Column(db.String(10))
