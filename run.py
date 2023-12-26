from flask import Flask, render_template, request, redirect
import mysql.connector  # Import MySQL connector


app = Flask(__name__)

# Database connection configuration
db = mysql.connector.connect(
    #credentials
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
    col_names = [desc[0] for desc in cursor.description] 

    return render_template("index.html", data=results,col_names=col_names)  # Pass data to template

@app.route("/process_data",methods=["POST"])
def send_data():

    entries = int(request.form["input_entries"]) #linked to html name attribute

    #did we actually forget the insert statement syntax :lol
    sql = "INSERT INTO hwcc_entrants (total_entrants) VALUES (%s)" #note entrant_count is taken from above var
    # Execute SQL statement
    with db.cursor() as cursor:
        cursor = db.cursor()
        cursor.execute(sql, (entries,)) #adding comma to introduce a tuple?
        db.commit()
    
    # # Close connections - with takes care of cursor.close
    # cursor.close()
    ## intentionally removed this to keep db connections open otherwise unexpected results?
    # db.close()


    return redirect("/") #redirection after submission

@app.route("/delete_records", methods=["POST"])
def delete_records():
    record_ids = request.form.getlist('record_ids')
    if record_ids:
        for record_id in record_ids:
            # Check if the checkbox is selected
            checkbox_value = request.form.get("record_ids_{row.id}")
          
            # Delete the record
            with db.cursor() as cursor_delete:
                sql_delete = "DELETE FROM hwcc_entrants WHERE record_id = %s"
                for record_id in record_ids:
                    cursor_delete.execute(sql_delete, (record_id,))
                db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)



