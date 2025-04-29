import Header from "./Header";
import Pie_Chart from "./Pie_Chart";
import { Row, Col, Tooltip, Divider} from "antd";
import {InfoCircleOutlined} from '@ant-design/icons';

export default function Graphs(props:{confidence:string[];}) {  

    const num_pies = props.confidence.length/2;
    const col_span = 24/num_pies;
    var viewport_min_width = 300*num_pies;
    // `{viewport_min_width}px`

    return (
      <div style={{minWidth:'720px'}}>        

        <div style={{border:'3px solid #D3D3D3', padding:'10px'}}>  

          <Row justify="center" style={{fontSize: 18, marginTop:20,fontWeight:'bold', color:'black'}}>
              AI GENERATED
          </Row> 

          <Row justify="center" style={{fontSize: 18, marginTop:5,fontWeight:'bold', color:'black'}}>
          DISTRIBUTION OF ON-SCREEN APPEARANCES 
          </Row>
              
          <Row >
            
            {Array(num_pies).fill(true).map((_, i) => <Col span={col_span}><Pie_Chart confidence = {props.confidence.slice(i*2, i*2+2)} filmID={(i+1).toString()} /> </Col>)}
          
          </Row>  
          
          <Divider/>

          {num_pies>1? 
          <Row style={{marginTop:30}}>

          <Col span={11}>
            <Row justify="center">
              <Tooltip placement="top" title={"We used the same AI gender model as in the films to recognize the perceived gender of human faces in a test dataset, for which we knew the actual gender."}>
              AI Gender Bias in Test Faces <InfoCircleOutlined /> :
              </Tooltip>
            </Row>

            <div id='plot_bar_gender' className="bk-root"></div>
          </Col>

          <Col span={1}></Col>

          <Col span={11}>
            <Row justify="center">
              <Tooltip placement="top" title={"We used the same AI age model as in the films to recognize the perceived age of human faces in a test dataset, for which we knew the actual age."}>
              AI Age Bias in Test Faces <InfoCircleOutlined /> :
              </Tooltip>
            </Row>

            <div id='plot_bar_age' className="bk-root"></div>
          </Col>
        </Row>:
        
          <div>
          <Row justify="center">
            <Tooltip placement="top" title={"We used the same AI gender model as in the films to recognize the perceived gender of human faces in a test dataset, for which we knew the actual gender."}>
            AI Gender Bias in Test Faces <InfoCircleOutlined /> :
            </Tooltip>
          </Row>
          <Row justify="center">
          <div id='plot_bar_gender' className="bk-root"></div>        
          </Row>
          <Row justify="center"  style={{marginTop:30}}>
            <Tooltip placement="top" title={"We used the same AI age model as in the films to recognize the perceived age of human faces in a test dataset, for which we knew the actual age."}>
            AI Age Bias in Test Faces <InfoCircleOutlined /> :
            </Tooltip>
          </Row>
          <Row justify="center">
          <div id='plot_bar_age' className="bk-root"></div>   
          </Row>       
          </div> 
          }          

        </div>
      </div>
    );
}
