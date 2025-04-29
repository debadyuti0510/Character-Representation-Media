from flask import Flask, render_template, send_from_directory
from flask_cors import CORS, cross_origin
from api import api

app = Flask(
    __name__,
    static_folder="frontend/build/static",
    template_folder="frontend/build",
)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.register_blueprint(api)

@app.route("/",defaults={'path': ''})
@app.route('/<path:path>')
@cross_origin()
def catch_all(path):
    return render_template("index.html")
    # return send_from_directory(app.template_folder, "index.html")



if __name__ == "__main__":
    app.run(debug=True)
