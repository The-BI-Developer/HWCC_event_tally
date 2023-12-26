from flask import Flask, render_template
import mysql.connector  # Import MySQL connector

app = Flask(__name__)

# Database connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="itookurjob",
    password="dalit",
    database="hwcc"
)

@app.route("/")
def display_table():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hwcc_entrants")
    results = cursor.fetchall()  # Fetch all rows
    return render_template("index.html", data=results)  # Pass data to template

if __name__ == "__main__":
    app.run(debug=True)
