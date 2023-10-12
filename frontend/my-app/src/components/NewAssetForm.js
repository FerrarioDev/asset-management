import React from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";
import axios from "axios";
import { API_URL } from "../constants";

class NewAssetForm extends React.Component {
  state = {
    id: "",
    model: "",
    user: "",
    asset_number: 0,
    serial_number: "",
    disk_serialnumber: "",
    device_type: "desktop", // Default to "desktop"
  };

  componentDidMount() {
    if (this.props.asset) {
      const {
        id,
        model,
        user,
        asset_number,
        serial_number,
        disk_serialnumber,
        device_type,
      } = this.props.asset;
      this.setState({
        id,
        model,
        user,
        asset_number,
        serial_number,
        disk_serialnumber,
        device_type,
      });
    }
  }

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  createAsset = (e) => {
    e.preventDefault();
    axios
      .post(API_URL, this.state)
      .then(() => {
        this.props.regetState();
        this.props.toggle();
      })
      .catch((error) => {
        console.error("API Request Error:", error);
      });
  };

  editAsset = (e) => {
    e.preventDefault();
    axios
      .put(`${API_URL}/${this.state.id}/`, this.state)
      .then(() => {
        this.props.regetState();
        this.props.toggle();
      })
      .catch((error) => {
        console.error("API Request Error:", error);
      });
  };

  defaultIfEmpty = (value) => {
    return value === "" ? "" : value;
  };

  render() {
    return (
      <Form onSubmit={this.props.asset ? this.editAsset : this.createAsset}>
        <FormGroup>
          <Label for="id">Asset ID:</Label>
          <Input
            type="text"
            name="id"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.id)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="model">Model:</Label>
          <Input
            type="text"
            name="model"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.model)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="user">User:</Label>
          <Input
            type="text"
            name="user"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.user)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="asset_number">Asset Number:</Label>
          <Input
            type="number"
            name="asset_number"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.asset_number)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="serial_number">Serial Number:</Label>
          <Input
            type="text"
            name="serial_number"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.serial_number)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="disk_serialnumber">Drive Serialnumber:</Label>
          <Input
            type="text"
            name="disk_serialnumber"
            onChange={this.onChange}
            value={this.defaultIfEmpty(this.state.disk_serialnumber)}
          />
        </FormGroup>
        <FormGroup>
          <Label for="device_type">Device Type:</Label>
          <Input
            type="select" // Change to a select input for choices
            name="device_type"
            onChange={this.onChange}
            value={this.state.device_type}
          >
            <option value="desktop">Desktop</option>
            <option value="laptop">Laptop</option>
          </Input>
        </FormGroup>
        <Button>Send</Button>
      </Form>
    );
  }
}

export default NewAssetForm;
