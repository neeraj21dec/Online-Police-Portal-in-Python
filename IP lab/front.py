from flask import Flask , request, render_template
import MySQLdb


app = Flask(__name__)



@app.route('/')
def index():
  return render_template("front.html")

@app.route('/register/')
def reg():
  return render_template("register.html")

@app.route('/adduser/' ,methods=['GET', 'POST'])
def add():
    db=MySQLdb.connect("localhost","root","12345","py" )
    sor= db.cursor()
    
    if request.method == 'POST':
     result=request.form['guess']
     if request.form['guess']=='police': 
     
        name=request.form['name']
        mail=request.form['mail']
        pwd=request.form['pwd']
        mobno=request.form['mobno']
        post=request.form['post']
        stname=request.form['stname']
        address=request.form['address']
        



        
        
        query = "INSERT INTO police (name,mail,pwd,mobno,post,stname,address) VALUES (%s,%s,%s,%s,%s,%s,%s)"
     
       
        try:
         sor.execute(query, (name,mail,pwd,mobno,post,stname,address))
         db.commit()
        except:
         print("not executed")   
         db.rollback()   
        
        return "Registration success!!"
        
@app.route('/policepage/')
def policepage():
  return render_template("policepage.html")

@app.route('/events/')
def events():
  return render_template("events.html")
    
@app.route('/records/')
def records():
  return render_template("records.html")   
    
@app.route('/officers/')
def officers():
  return render_template("officers.html") 

@app.route('/solved/')
def solved():
  return render_template("solved.html") 

@app.route('/unsolved/')
def unsolved():
  return render_template("unsolved.html") 

@app.route('/messages/')
def messages():
  return render_template("messages.html") 

@app.route('/profile/')
def profile():
  return render_template("profile.html") 

@app.route('/eventshow/')
def eventshow():
  return render_template("eventshow.html") 

@app.route('/criminaldetails/')
def criminaldetails():
  return render_template("criminaldetails.html") 


@app.route('/updatenews/')
def updatenews():
  return render_template("updatenews.html") 

@app.route('/casedetails/')
def casedetails():
  return render_template("casedetails.html")

@app.route('/sentmssg/')
def sentmssg():
  return render_template("sentmssg.html")


@app.route('/trash/')
def trash():
  return render_template("trash.html")

@app.route('/stations/')
def stations():
  return render_template("stations.html")

@app.route('/auctions/')
def auc():
  return render_template("auctions.html")

@app.route('/logincheck/',methods=['GET', 'POST'])
def log():
    db=MySQLdb.connect("localhost","root","12345","py" )
    sor= db.cursor()
    if request.method == 'POST':
     mobno=request.form['mobno']
     
     sql = "SELECT * FROM police WHERE mobno > '%s'" % (mobno)
     try:
      sor.execute(sql)    
      results = sor.fetchall()
      if results!="null":
          return render_template("policepage.html")
      else:
         return "Wrong Details"
     except:
       print ("Error: unable to fecth data")

if __name__ == '__main__':
   app.run(debug=True)                  