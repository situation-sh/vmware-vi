# HostPortGroupPort

A Port data object type is a runtime representation of network connectivity between a network service or virtual machine and a virtual switch.  This is different from a port group in that the port group represents the configuration aspects of the network connection. The Port object provides runtime statistics. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The linkable identifier.  | [optional] 
**mac** | **List[str]** | The Media Access Control (MAC) address of network service of the virtual machine connected on this port.  | [optional] 
**type** | **str** | The type of component connected on this port.  Must be one of the values of *PortGroupConnecteeType_enum*.  | 

## Example

```python
from vmware_vi.models.host_port_group_port import HostPortGroupPort

# TODO update the JSON string below
json = "{}"
# create an instance of HostPortGroupPort from a JSON string
host_port_group_port_instance = HostPortGroupPort.from_json(json)
# print the JSON string representation of the object
print HostPortGroupPort.to_json()

# convert the object into a dict
host_port_group_port_dict = host_port_group_port_instance.to_dict()
# create an instance of HostPortGroupPort from a dict
host_port_group_port_form_dict = host_port_group_port.from_dict(host_port_group_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


