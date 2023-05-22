from flask import *
from database import *
import uuid
public=Blueprint('public',__name__)

@public.route('/')
def welcome():
    return render_template('welcome.html')

@public.route('/registration',methods=['post','get'])
def registration():
    if 'submit' in request.form:
        fn=request.form['first_name']
        ln=request.form['last_name']
        hn=request.form['house_name']
        pl=request.form['place']
        pin=request.form['pincode']
        ph=request.form['phone']
        em=request.form['email']
       # un=request.form['uname']
        #pwd=request.form['password']
        q="insert into login values(null,'%s','%s','pending')"%(em,ph)
        res=insert(q)
        print(res)
        s="insert into customers values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(res,fn,ln,hn,pl,pin,ph,em)
        t=insert(s)
        print(t)
        fl=request.files['file']
        path="static/uploads/"+str(uuid.uuid4())+fl.filename
        fl.save(path)
        u="insert into files values(null,'%s','%s','user_file')"%(t,path)
        v=insert(u)
        print(u)
    return render_template('registration.html')

@public.route('/login',methods=['post','get'])
def login():
    if 'login' in request.form:
        un=request.form['username']
        pwd=request.form['password']
        print(un,pwd)
        q="select * from login where username='%s' and password='%s'"%(un,pwd)
        res=select(q)
        if res: 
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.adminhome'))
                 
    return render_template('login.html')