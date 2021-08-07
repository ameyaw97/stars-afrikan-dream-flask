from flask_wtf import FlaskForm,Form
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,IntegerField,DateField 
from wtforms.validators import DataRequired,Email,Length,ValidationError

class registration(FlaskForm):
    fullname= StringField('Full Name',validators= [DataRequired(),Length(min=4,max =30)])
    email = StringField('Email',validators= [DataRequired(),Email()])
    Submit = SubmitField('Sign Up')
    
   # def validate_email(self,email):
     #   user = User.query.filter_by(email=email.data).first()
      #  if user:
      #      raise ValidationError('This email is already taken please choose another one!')
        
    #def validate_Fullname(self,fullname):
    #    user = User.query.filter_by(fullname=fullname.data).first()
    #    if user:
     #       raise ValidationError('This Name is already taken please choose another one!')
            
    
    
class Enroll(FlaskForm):
    fullname= StringField('Full Name',validators= [DataRequired()] )
    gender = SelectField('Gender',choices=[('female', 'female'),('male', 'male')])
    dob= DateField('Date of Birth', format='%d/%m/%Y',validators= [DataRequired()]) 
    age= IntegerField('Age',validators= [DataRequired()])
    number= IntegerField('Phone Number',validators= [DataRequired()])
    email = StringField('Email',validators= [Email(),DataRequired()])
    location= StringField('Location',validators= [DataRequired()])
    digital= StringField('Digital Address',validators= [DataRequired()])
    landmark= StringField('Landmark',validators= [DataRequired()])
    guard = StringField('Guardian',validators= [DataRequired()])
    guardnum= StringField('Guardians contact',validators= [DataRequired()])
    #Emergency
    
    submit = SubmitField('Enroll')
    clear = SubmitField('Clear')