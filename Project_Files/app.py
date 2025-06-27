# app.py

from flask import Flask
from routes.assistant_router import assistant_bp

app = Flask(_name_)

# Register blueprint
app.register_blueprint(assistant_bp, url_prefix='/api/assistant')

if _name_ == '_main_':
    app.run(debug=True, port=5000)