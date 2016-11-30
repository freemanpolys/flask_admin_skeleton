from livereload import Server
from app import app

# app.run(host='0.0.0.0', port=8080, debug=True)
app.debug = True
server = Server(app.wsgi_app)
# server.watch
server.serve()

