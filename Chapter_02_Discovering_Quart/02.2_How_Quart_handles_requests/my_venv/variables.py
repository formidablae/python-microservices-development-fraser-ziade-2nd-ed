from quart import Quart

app = Quart(__name__)

@app.route("/person/<int:person_id>")
def person(person_id):
    return {"Hello": person_id}

app.run()
