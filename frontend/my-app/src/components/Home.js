import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import AssetList from "./AssetList";
import NewAssetModal from "./NewAssetModal";

import axios from "axios";

import { API_URL } from "../constants";

class Home extends Component {
    state = {
        assets: []
    }

    componentDidMount(){
        this.resetState();
    };

    getAssets = () => {
        axios.get(API_URL).then(res => this.setState({ assets: res.data})).catch(error => {
            if (error.response) {
              // The request was made, but the server responded with a status code outside the 2xx range
              console.error("Response Error:", error.response.data);
            } else if (error.request) {
              // The request was made, but no response was received
              console.error("Request Error:", error.request);
            } else {
              // Something happened in setting up the request that triggered an error
              console.error("Request Setup Error:", error.message);
            }
          });    
    };

    resetState = () => {
        this.getAssets();
    };

    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <Row>
                    <Col>
                        <AssetList assets={this.state.assets} resetState={this.resetState}/>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <NewAssetModal create={true} resetState={this.resetState} />
                    </Col>
                </Row>
            </Container>
        );
    };
}

export default Home;