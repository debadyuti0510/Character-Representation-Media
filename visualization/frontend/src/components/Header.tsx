import {Row} from "antd";

export default function Header() {  

    return (
      <div>
        <Row style={{margin:10, fontSize: 20}}>
          Contact: &nbsp; email &nbsp;
        </Row> 

        <Row style={{margin:10, fontSize: 20}}>
          We estimated the distribution of the on-screen appearances for the &nbsp; <b>full-length</b> &nbsp; films. 
        </Row> 

        <Row style={{margin:15, fontSize: 20}}>
          The graphs and some texts are &nbsp; <b>interactive</b>. Hover over them and more info will pop up.
        </Row>       

      </div>
    );
}
