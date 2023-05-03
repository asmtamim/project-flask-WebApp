# Flask Web-application
#### A simple web application using Flask that allows users to upload and download files asynchronously.

## Instruction of how to run this project

- Download the 'project-flask-WebApp' from GitHub.
- Follow the README.md file accordingly.
- Run the flask_wa.sql file into a MySQL database environment, I prefer- xampp 'phpmyadmin'.
- Database set-up: MYSQL_HOST = 'localhost', MYSQL_USER = 'root', MYSQL_PASSWORD = '117734', MYSQL_DB = 'flask_wa'.
- Open Flask-Web-App as project folder into any python IDE, I prefer 'VS Code' or 'PyCharm'.
- Create a Virtual Environment inside that folder.
- Install pip and other necessary library packages to run this program.
- Then run the program (run 'python .\main.py' in terminal).
- Check if this- 'MySQL db is connected! ***' string is printed in the terminal to make sure the program is connected to the database.

### User interactions and maneuvers
- Click to Login button. 
- Login to the system with credentials from 'users' table of 'flask_wa' database.
- View the files loaded from the database.
- Delete or DOWNLOAD existing files from the database.
- Upload any types ('txt', 'pdf', 'png', 'jpg', 'jpeg') of file from upload section, which will be uploaded to local server and location-info will be stored in DB.
- Again see the instantly updated list of available files and delete or DOWNLOAD asynchronously.

#### Important python library packages to install

- pip — is the Package Installer for Python.
- flask — 'pip install flask'
- Flask-MySQL — 'pip install flask-mysql'
- mysql-connector — 'pip install mysql-connector-python'
- Flask-Uploads — 'pip install Flask-Uploads'
- flask-login — 'pip install flask-login'
- WTForms — 'pip install WTForms'
- aiofiles — 'pip install aiofiles'
- And some other library packages which is installed by default with flask like — Jinja, werkzeug, asyncio etc.
