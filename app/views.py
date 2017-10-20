from app import app

#Mappings from Routes / and /index to Python Flask handler below
@app.route("/")
@app.route("/index")
def index():
	return "Hello, World!"