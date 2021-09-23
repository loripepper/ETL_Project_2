from flask import Flask, render_template
import pymongo

app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.crashData_db
crashes = db.crashes

@app.route("/")
def index():
   
    crash_list = list(crashes.find())
    # print(crash_list)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", crashes=crashes)


if __name__ == "__main__":
    app.run(debug=True)