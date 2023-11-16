# ArrayOfDistributedVirtualSwitchPortConnection

A boxed array of *DistributedVirtualSwitchPortConnection*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualSwitchPortConnection]**](DistributedVirtualSwitchPortConnection.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_switch_port_connection import ArrayOfDistributedVirtualSwitchPortConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualSwitchPortConnection from a JSON string
array_of_distributed_virtual_switch_port_connection_instance = ArrayOfDistributedVirtualSwitchPortConnection.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualSwitchPortConnection.to_json()

# convert the object into a dict
array_of_distributed_virtual_switch_port_connection_dict = array_of_distributed_virtual_switch_port_connection_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualSwitchPortConnection from a dict
array_of_distributed_virtual_switch_port_connection_form_dict = array_of_distributed_virtual_switch_port_connection.from_dict(array_of_distributed_virtual_switch_port_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


