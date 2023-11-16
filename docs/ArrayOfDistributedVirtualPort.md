# ArrayOfDistributedVirtualPort

A boxed array of *DistributedVirtualPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DistributedVirtualPort]**](DistributedVirtualPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_distributed_virtual_port import ArrayOfDistributedVirtualPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDistributedVirtualPort from a JSON string
array_of_distributed_virtual_port_instance = ArrayOfDistributedVirtualPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfDistributedVirtualPort.to_json()

# convert the object into a dict
array_of_distributed_virtual_port_dict = array_of_distributed_virtual_port_instance.to_dict()
# create an instance of ArrayOfDistributedVirtualPort from a dict
array_of_distributed_virtual_port_form_dict = array_of_distributed_virtual_port.from_dict(array_of_distributed_virtual_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


