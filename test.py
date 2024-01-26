from sqlalchemy import create_engine
from market import db, app
from market.models import Item

#items = [
 #   {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
  #  {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
   # {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
#]

# Create the engine
with app.app_context():
    # Create the database tables (if they don't exist)
    db.drop_all()
    

    # Insert items into the database
    #for item in items:
     #   new_item = Item(
      #      name=item['name'],
       #     barcode=item['barcode'],
        #    price=item['price'],
         #   description="nice product",
          #  count=10
        #)
        #db.session.add(new_item)

    #db.session.commit()
