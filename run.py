from app import app

app.run(debug=True)
app.config.from_object("config")