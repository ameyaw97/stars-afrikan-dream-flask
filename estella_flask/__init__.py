from flask import Flask,redirect,url_for,render_template,request,redirect,flash
from flask_bootstrap import Bootstrap
from estella_flask.inputform import Enroll


app=Flask(__name__)

bootstrap=Bootstrap(app)
app.config['SECRET_KEY']= "qmwrtyuihe!@$^!@#@Y@&p098765wrewytwuwvsgdvgxgdnbxhbdbdjdhssf"
@app.route('/home')
@app.route('/',methods=['GET','POST'])
def home():
   # if request.method=='POST':
        # Handle POST Request here
       # return render_template('index.html')
    return render_template('index.html')


@app.route('/shop',methods=['GET','POST'])
def shop():
   # if request.method=='POST':
        # Handle POST Request here
       # return render_template('index.html')
    return render_template('shop.html')


@app.route('/blog',methods=['GET','POST'])
def blog():
   # if request.method=='POST':
        # Handle POST Request here
       # return render_template('index.html')
    return render_template('blog.html')
 
@app.route('/post1',methods=['GET','POST'])
def post1():
       return render_template('post1.html')
       

@app.route('/about',methods=['GET','POST'])
def about():
   # 
        # Handle POST Request here
       # return render_template('index.html')
    return render_template('about.html')
 
 
@app.route('/enroll',methods=['GET','POST'])

def enroll():
   form = Enroll()
   if form.validate_on_submit() and form.submit.data:
        #hashed_pwd = bcrypt.generate_password_hash(form.Password.data)
        #user = User(FullName = form.FullName.data, Email =form.Email.data,Password= hashed_pwd)
        #db.session.add(user)
        #db.session.commit()
       flash(f'Welcome {form.fullname.data} your application has been received you will hear from us', 'success') 

       return render_template('enroll.html',form=form)

   elif form.clear.data :
        return redirect(url_for('enroll'))
   elif request.method=='POST' and form.submit.data:
        flash(f'Oops check your entry and try again','danger')
        return redirect( url_for('enroll'))
                
   else:
       return render_template('enroll.html',form=form)  #redirect( url_for('enroll'))
     

@app.route('/estella',methods=['GET','POST'])
def estella():
       return render_template('estella.html')
    
    
    
@app.route('/customer',methods=['GET','POST'])
def customer():
       return render_template('customer.html')
    
    
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
    
