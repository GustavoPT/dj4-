from settings import *
from models import User

specialCharacters = ['$', '#', '@', '!', '*','%','^','&']

class RegistrationForm(FlaskForm):
    email = StringField('email', [validators.Length(min=6, max=35)])
    password = PasswordField('password', [
        validators.DataRequired()
    ])
    submit = SubmitField('Register')

    def validate_credentials(self,request,db):
        password = request.form['password']
        email = request.form['email']
        is_proper_email,result_message = is_proper_email(email)
        
        if is_proper_email == False:
            return False,result_message
        
        is_proper_password,result_message = is_proper_password(password)

        if is_proper_password == False:
            return False,result_message
    
        return True    
    def is_proper_email(email,db):

        exists = db.session.query(User.id).filter_by(email=email).scalar() is not None

        if exists == True:
            errorMessage = "Someone already exists with that email"
            return False,errorMessage
        if '@' not in email:
            errorMessage = "Email must have @ to be considered a valid email"
            return False,errorMessage
        return True,""
    def is_proper_password(password):
        if len(password) < 4:
            flash("Password must be of length greater than 4",'error')
            return False
        return True,""

class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    def validate_credentials(request):
        login_form = request.loginForm

        user_in_db = User.query.filter_by(email=login_form.email.data).first()

        if user_in_db and (user_in_db.password == login_form.password.data):
            return True,user_in_db               
        else:
            return False,"That username could not be found/password/username are incorrect" 
