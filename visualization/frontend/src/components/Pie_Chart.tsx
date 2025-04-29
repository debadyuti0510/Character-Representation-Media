import { Row, Col, Tooltip} from "antd";
import {InfoCircleOutlined} from '@ant-design/icons';

export default function Pie_Chart(props:
    {
        filmID:string;
        confidence:string[];
    }) {  

    return (
      <div >       

        <Row justify="center" style={{marginTop:15, fontSize: 16, fontWeight:'bold', color:'black'}}>
        Film {props.filmID}
        </Row>              

        <div id={`plot_f${props.filmID}`} className="bk-root"></div>      

        <Row  justify="end" style={{marginBottom:0, marginTop:15, marginRight:10, fontStyle:'bold', color:'black'}}> 
        <Col pull={5}>               
        <Tooltip placement="top" title={"Average confidence of the AI in recognising the perceived gender or age of the appeared faces in this film"}>
        Film {props.filmID} AI Confidence <InfoCircleOutlined />
        </Tooltip>
        </Col>
        </Row>

        <Row  justify="end" style={{marginBottom:0, marginTop:15, marginRight:10, fontStyle:'bold', color:'black'}}>
        <Col pull={5}>
            for Gender Recognition: {props.confidence[0]}%
        </Col> 
        </Row>

        <Row  justify="end" style={{marginBottom:0, marginTop:15, marginRight:10, fontStyle:'bold', color:'black'}}>
        <Col pull={5}>
            for Age Recognition: {props.confidence[1]}%
        </Col> 
        </Row>       

      </div>
    );
}
