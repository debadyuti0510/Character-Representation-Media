import Graphs from "../components/Graphs";
import Header from "../components/Header";
import { URL_HEAD } from "../utils/endpoint";

import { Row, Col} from "antd";

import useSWR from "swr";

export default function Task() {

    // GET DATA FROM "api/user_film_data"
    const fetcher = (url: any) => fetch(url).then((res) => res.json());
    const url = URL_HEAD + "api/user_film_data";
    const userfilmdata = useSWR(url, fetcher);
    if (userfilmdata.error) return <div>Data Failed to Load</div>;
    if (!userfilmdata.data) {
      return (
        <div>
          <div>Loading</div>
        </div>
      );
    }
    var graphs = userfilmdata.data["graphs"];
    var confidence = userfilmdata.data["confidencescores"];
    var num_pies = graphs.length - 2;

    // SHOW GRAPHS IN WINDOW
    for (let i = 0; i < num_pies; i++) {
      var g = window.document.getElementById("plot_f"+(i+1).toString());
      if (g!==null){
        g.innerHTML = "";
      }
      (window as any).Bokeh.embed.embed_item(graphs[i], 'plot_f'+(i+1).toString());
    }
    var g = window.document.getElementById('plot_bar_gender');
      if (g!==null){
        g.innerHTML = "";
      }
    (window as any).Bokeh.embed.embed_item(graphs[num_pies], 'plot_bar_gender');
    var g = window.document.getElementById('plot_bar_age');
      if (g!==null){
        g.innerHTML = "";
      }
    (window as any).Bokeh.embed.embed_item(graphs[num_pies+1], 'plot_bar_age');
   
    var col_span = 5*(confidence.length/2);
    return (
      <div>  
        <Row > 
          <Col span={20}>
            <Header/>             
          </Col>
        </Row>  
        <Row>
          <Col span={col_span}>
            <Graphs confidence={confidence}/> 
          </Col>  
        </Row> 
      </div>
    );
}
