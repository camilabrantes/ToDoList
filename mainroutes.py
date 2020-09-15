from Flask import Blueprint,render_template
routes = Blueprint('routes',__name__)

@routes.route("/")
def homePage():
	items = [
			"Cook Dinner",
			"Wash Dishes",
			"Do Laundry",
			"Clean Room"
	]
	return render_template("homepage.html", todolist=items)
		