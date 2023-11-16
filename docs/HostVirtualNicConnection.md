# HostVirtualNicConnection

DataObject which provides a level of indirection when identifying VirtualNics during configuration.  This dataObject lets users specify a VirtualNic in terms of the portgroup/Dv Port the Virtual NIC is connected to. This is useful in cases where VirtualNic will be created as part of a configuration operation and the created VirtualNic is referred to in some other part of configuration. e.g: for configuring VMotion  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**portgroup** | **str** | Name of the portgroup to which the virtual nic is connected to.  If this parameter is set, use a virtual nic connected to a legacy portgroup.  ***Since:*** vSphere API 4.0  | [optional] 
**dv_port** | [**DistributedVirtualSwitchPortConnection**](DistributedVirtualSwitchPortConnection.md) |  | [optional] 
**op_network** | [**HostVirtualNicOpaqueNetworkSpec**](HostVirtualNicOpaqueNetworkSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic_connection import HostVirtualNicConnection

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicConnection from a JSON string
host_virtual_nic_connection_instance = HostVirtualNicConnection.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicConnection.to_json()

# convert the object into a dict
host_virtual_nic_connection_dict = host_virtual_nic_connection_instance.to_dict()
# create an instance of HostVirtualNicConnection from a dict
host_virtual_nic_connection_form_dict = host_virtual_nic_connection.from_dict(host_virtual_nic_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


