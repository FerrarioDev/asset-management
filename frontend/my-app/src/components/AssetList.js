import React, { Component } from "react";
import { Table } from "reactstrap";
import NewAssetModal from "./NewAssetModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal"

class AssetList extends Component {
    render() {
        const assets = this.props.asset;
        return (
            <Table dark>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Model</th>
                        <th>User</th>
                        <th>Asset Number</th>
                        <th>Serial Number</th>
                        <th>Disk Serial Number</th>
                        <th>Device Type</th>
                        <th>Registration</th>
                    </tr>
                </thead>
                <tbody>
                    {!assets || assets.length <= 0 ?( 
                        <tr>
                            <td colSpan="6" align="center">
                                <b>No assets here</b>
                            </td>
                        </tr>
                    ) : (  
                        assets.map(asset => (
                            <tr key={asset.id}>
                                <td>{asset.id}</td>
                                <td>{asset.model}</td>
                                <td>{asset.user}</td>
                                <td>{asset.asset_number}</td>
                                <td>{asset.serial_number}</td>
                                <td>{asset.disk_serialnumber}</td>
                                <td>{asset.device_type}</td>
                                <td>{asset.registrationDate}</td>
                                <td align="center">
                                    <NewAssetModal
                                        create={false}
                                        asset={asset}
                                        resetState={this.props.resetState}
                                    />
                                    &nbsp;&nbsp;
                                    <ConfirmRemovalModal
                                        pk={asset.id}
                                        resetState={this.props.resetState}
                                    />
                                </td>
                            </tr>
                        ))
                    )}
                </tbody>
            </Table>
        );
    };
}

export default AssetList;