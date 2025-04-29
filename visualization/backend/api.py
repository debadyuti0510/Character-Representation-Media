import json
import os
from os.path import dirname
from flask import Blueprint
import bokeh

from utils.visualization import get_onscreentime_graphs

DATA_PATH = os.path.join(dirname(dirname(__file__)), "backend/data")

api = Blueprint("api", __name__, url_prefix="/api")

## CALLED IN task.tsx
@api.route("/user_film_data", methods=["POST", "GET"])
def get_userdata():
    ##
    plots_n_confscores = get_onscreentime_graphs()
    graphs = []
    for i in range(len(plots_n_confscores)-3):
        graphs.append(bokeh.embed.json_item(plots_n_confscores[i], "plot_f"+str(i)))
    graphs.append(bokeh.embed.json_item(plots_n_confscores[len(plots_n_confscores)-3], "plot_bar_gender"))
    graphs.append(bokeh.embed.json_item(plots_n_confscores[len(plots_n_confscores)-2], "plot_bar_age"))

    return json.dumps({"graphs":graphs,"confidencescores":plots_n_confscores[len(plots_n_confscores)-1]}).replace("\\", "")

