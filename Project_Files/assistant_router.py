# routes/assistant_router.py

from flask import Blueprint
from controllers.assistant_controller import get_smart_city_advice

assistant_bp = Blueprint('assistant', _name_)

# Define a route to handle smart city assistant queries
assistant_bp.route('/ask', methods=['POST'])(get_smart_city_advice)

