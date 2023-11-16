# VnicPortArgument

This argument records a Virtual NIC device that connects to a DVPort.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vnic** | **str** | The Virtual NIC devices that were using the DVports.  ***Since:*** vSphere API 4.0  | 
**port** | [**DistributedVirtualSwitchPortConnection**](DistributedVirtualSwitchPortConnection.md) |  | 

## Example

```python
from vmware_vi.models.vnic_port_argument import VnicPortArgument

# TODO update the JSON string below
json = "{}"
# create an instance of VnicPortArgument from a JSON string
vnic_port_argument_instance = VnicPortArgument.from_json(json)
# print the JSON string representation of the object
print VnicPortArgument.to_json()

# convert the object into a dict
vnic_port_argument_dict = vnic_port_argument_instance.to_dict()
# create an instance of VnicPortArgument from a dict
vnic_port_argument_form_dict = vnic_port_argument.from_dict(vnic_port_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


