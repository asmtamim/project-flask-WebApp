from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, Response
from flask_mysqldb import MySQL
import mysql.connector
import aiofiles
import os


# Create flask app
app = Flask(__name__)
app.secret_key = "tamim.webdev"

# MySQL database connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '117734'
app.config['MYSQL_DB'] = 'flask_wa'

# files = UploadSet('files', ALL)
# configure_uploads(app, files)
# mysql = MySQL(app)

# File upload configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

mysql = mysql.connector.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'], password=app.config['MYSQL_PASSWORD'], 
                                database=app.config['MYSQL_DB'])

cursor = mysql.cursor()

if (mysql.is_connected()):
    print("MySQL db is connected! ***")
else:
    print("MySQL db is NOT connected! ***")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    cursor.execute("SELECT * FROM files")
    data = cursor.fetchall()
    return render_template('home.html', username=session['username'], data=data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    text = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        query1 = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query1, (username, password))
        record = cursor.fetchone()
        if record:
            session['Logged in'] = True
            session['username'] = record[1]
            return redirect(url_for('home'))
        else:
            text = "Incorrect username/password. Try again!"
    
    return render_template('login.html', text=text)

@app.route('/logout')
def logout():
    session.pop('Logged in', None)
    session.pop('username', None)
    return redirect(url_for('login'))


# File upload
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)
    query2 = "INSERT INTO files (file_name, file_path, file_type) VALUES (%s, %s, %s)"
    cursor.execute(query2, (filename, file_path, file.content_type))
    mysql.commit()

    flash("File uploaded successfully!")
    return redirect(url_for('home'))


# File delete
@app.route('/delete_file/<filename>', methods=['GET', 'POST'])
def delete_file(filename):
    cursor.execute("SELECT * FROM files WHERE file_name = %s", (filename,))
    file = cursor.fetchone()
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file[1])
        os.remove(filepath)
        cursor.execute("DELETE FROM files WHERE file_name = %s", (filename,))
        mysql.commit()
        flash('File has been deleted successfully!')
    else:
        flash('File not found!')

    return redirect(url_for('home'))


# File download using "async"
@app.route('/download/<filename>')
async def download_file(filename):
	file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	if os.path.exists(file_path):
		async with aiofiles.open(file_path, mode='rb') as f:
			contents = await f.read()
		return Response(contents, mimetype="application/octet-stream",
			headers={"Content-disposition": f"attachment; filename={filename}"}
		)
	else:
		flash("The requested file does not exist.")
		return redirect(url_for('home'))


# App run
if __name__ == '__main__':
    app.run(debug=True)

