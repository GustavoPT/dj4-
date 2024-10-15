from settings import *
from forms import *
from models import * 

login_manager = LoginManager()
login_manager.init_app(app)
#dry
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
@app.route('/', methods=['GET', 'POST'])
def real_index():
    return redirect(url_for('index'))

@app.route('/products')
def index():
    products = Product.get_all_products()
    return render_template('products.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == 'GET':
        return render_template('authentication.html', action='login', login_form=login_form, registration_form=registration_form)

    elif request.method == 'POST':
        validate_credentials,db_user_or_error_message = request.login_form.validate_credentials(request)

        if validate_credentials == True: 
            login_user(db_user_or_error_message, remember=login_form.remember.data)
            flash("You are now logged in", 'success')
            return 
        else:
            flash(db_user_or_error_message, 'error')
            return 
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == "POST":

        result,result_message  =  request.form.validate_credentials(request)

        if result == True:
            new_user = User(password=request.registration_form.password.data, email=request.registration_form.email.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            result_message = "You were successfully registered"
            flash(result_message, 'success')
            return redirect(url_for("index"))
        else:
            flash(result_message, 'error')
            return redirect(url_for("register"))
        
    return render_template('authentication.html', action='register', login_form=login_form, registration_form=registration_form)

@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out", 'success')
    return redirect(url_for('index'))

@app.route('/user_profile', methods=['GET', 'POST'])
@login_required
def user_profile():
    if current_user.is_authenticated:
        user_shippings = current_user.user_shippings
        user_cards = current_user.user_cards

    if request.method == 'POST':
        user_db = User.query.filter_by(id=current_user.id).first()
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        physical_address = request.form['physical_address']
        current_user.name = name
        
        
        if "@" in email:
            current_user.email = email
        else: 
            flash('Email must have @','error')
            return redirect(url_for('user_profile'))
        if len(password) < 4:
            flash("Password must be of length greater than 4",'error')
            return redirect(url_for('user_profile'))
        if not any(c in specialCharacters for c in password):
            flash('Password must have atleast one special character','error')
            return redirect(url_for('user_profile'))
        current_user.password = password
        current_user.physical_address = physical_address
        user_db.name = name
        user_db.email = email
        user_db.password = password
        user_db.physical_address = physical_address
        db.session.commit()
        flash('successfully updated', 'success')
        return redirect(url_for('user_profile'))

    return render_template('user_profile.html', user_shippings=user_shippings, user_cards=user_cards)

@app.route('/product/<int:id>')
def product(id):
    product = Product.query.filter_by(id=id).first()
    author = product.authorName

    users = User.query.all()
    user_map = {}
    for user in users:
        user_map[user.id] = user.name

    order_count = 0
    if hasattr(current_user, 'id'):
        order_count = Order.query.filter_by(product_id=id,user_id=current_user.id).count()

    has_ordered = order_count > 0
    average_rating = 0
    total_rating = 0

    return render_template('product.html', product=product, author=author, average_rating=average_rating)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cartItems = []

    user_id = current_user.id
    # check thru products for the product with the specified id 
    # check thru the product copy for the product copy with the id
    product = Cart(user_id=user_id, product_id=product_id, quantity=1)
    db.session.add(product)
    db.session.commit()

    flash('Product added to cart', 'success')
    return redirect(url_for('index'))


@app.route('/checkout',methods=['GET', 'POST'])
def cart():
    
    if request.method == 'POST':

        user_id = current_user.id

        orders = Cart.query.filter_by(user_id=user_id).all()

        # logic to checkout 
        # make a transaction 
        # for all the items in user cart 
        # 
        #
        return render_template('products.html',order=orders)

    # logic to get all in cart 

    user_id = current_user.id
    user_cart = Cart.query.filter_by(user_id=user_id).all()
    user_products = []
    total_price = 0

    for product in user_cart:
        product_id = product.product_id
        product = Product.query.filter_by(id=product_id).first()
        total_price = product.price + total_price
        user_products.append(product)

    cart_products = len(user_products)

    return render_template('checkout.html', total_price=total_price, products=user_products, cart_products=cart_products)

if __name__ == '__main__':
    app.run(debug=True)
