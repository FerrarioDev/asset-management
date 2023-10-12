import React, { Component, Fragment } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

class ConfirmRemovalModal extends Component {
    state = {
        modal: false
    };

    toggle = () => {
        this.setState(previous => ({
          modal: !previous.modal
        }));
    };

    deleteAsset = pk => {
        axios.delete(API_URL + pk).then(() => {
            this.props.resetState();
            this.toggle();
        }).catch(error => {
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

    render() {
        return (
            <Fragment>
            <Button color="danger" onClick={() => this.toggle()}>
              Remove
            </Button>
            <Modal isOpen={this.state.modal} toggle={this.toggle}>
              <ModalHeader toggle={this.toggle}>
                Do you really wanna delete this asset?
              </ModalHeader>
    
              <ModalFooter>
                <Button type="button" onClick={() => this.toggle()}>
                  Cancel
                </Button>
                <Button
                  type="button"
                  color="primary"
                  onClick={() => this.deleteAsset(this.props.id)}
                >
                  Yes
                </Button>
              </ModalFooter>
            </Modal>
          </Fragment>
        );
    };
}

export default ConfirmRemovalModal;