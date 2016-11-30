import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
#SQLALCHEMY_DATABASE_URI = 'postgresql://root:password@localhost/myapp'

# Flask-WTF flag for CSRF
# CSRF_ENABLED = True

#------------------------------
# GLOBALS FOR APP Builder 
#------------------------------
# Uncomment to setup Your App name
#APP_NAME = "My App Name"

# Uncomment to setup Setup an App icon
#APP_ICON = "static/img/logo.jpg"


