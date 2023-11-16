# DistributedVirtualSwitchPortConnection

The *DistributedVirtualSwitchPortConnection* data object represents a connection or association between a *DistributedVirtualPortgroup* or a *DistributedVirtualPort* and one of the following entities: - Virtual machine virtual NIC   (*VirtualEthernetCardDistributedVirtualPortBackingInfo*) - Host virtual NIC (*HostVirtualNic*) - Physical NIC (*HostNetworkInfo*.*HostNetworkInfo.pnic*)    ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_uuid** | **str** | UUID of the switch (*DistributedVirtualSwitch*.*DistributedVirtualSwitch.uuid*).  ***Since:*** vSphere API 4.0  | 
**portgroup_key** | **str** | Key of the portgroup.  If specified, the connection object represents a connection or an association between a *DistributedVirtualPortgroup* and a Virtual NIC or physical NIC. In this case, setting the *DistributedVirtualSwitchPortConnection.portKey* is not necessary for a early-binding portgroup and is not allowed for a late-binding portgroup. The *DistributedVirtualSwitchPortConnection.portKey* property will be populated by the implementation at the time of port binding.  ***Since:*** vSphere API 4.0  | [optional] 
**port_key** | **str** | Key of the port.  If specified, this object represents a connection or an association between an individual *DistributedVirtualPort* and a Virtual NIC or physical NIC. See *DistributedVirtualSwitchPortConnection.portgroupKey* for more information on populating this property.  ***Since:*** vSphere API 4.0  | [optional] 
**connection_cookie** | **int** | Cookie that represents this *DistributedVirtualSwitchPortConnection* instance for the port.  The cookie value is generated by the Server. The Server ignores any value set by an SDK client.  The same cookie is present in the distributed virtual port configuration (*DistributedVirtualPort*.*DistributedVirtualPort.connectionCookie*) so that the Server can verify that the entity is the rightful connectee of the port.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_port_connection import DistributedVirtualSwitchPortConnection

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchPortConnection from a JSON string
distributed_virtual_switch_port_connection_instance = DistributedVirtualSwitchPortConnection.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchPortConnection.to_json()

# convert the object into a dict
distributed_virtual_switch_port_connection_dict = distributed_virtual_switch_port_connection_instance.to_dict()
# create an instance of DistributedVirtualSwitchPortConnection from a dict
distributed_virtual_switch_port_connection_form_dict = distributed_virtual_switch_port_connection.from_dict(distributed_virtual_switch_port_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

