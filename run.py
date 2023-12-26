from flask import Flask, render_template, request, redirect
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

@app.route("/process_data",methods=["POST"])
def send_data():
    entries = int(request.form["total_entrants"]) #linked to html name attribute
    sql = "INSERT INTO hwcc_entrants (entries) VALUES (%s)" #note entrant_count is taken from above var
    # Execute SQL statement
    cursor = db.cursor()
    cursor.execute(sql, (entries,)) #adding comma to introduce a tuple?
    db.commit()
    
    
    # Close connections
    cursor.close()
    db.close()

    return redirect("/") #redirection after submission

if __name__ == "__main__":
    app.run(debug=True)


