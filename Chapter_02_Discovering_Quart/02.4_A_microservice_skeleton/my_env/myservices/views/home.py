from quart import Blueprint

home = Blueprint("home", __name__)

@home.route("/")
def index():
    """Hone view.
    
    This view will return an empty JSON mapping.
    """
    return {}
