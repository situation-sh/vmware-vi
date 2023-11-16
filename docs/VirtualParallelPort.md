# VirtualParallelPort

This data object type represents a parallel port in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_parallel_port import VirtualParallelPort

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualParallelPort from a JSON string
virtual_parallel_port_instance = VirtualParallelPort.from_json(json)
# print the JSON string representation of the object
print VirtualParallelPort.to_json()

# convert the object into a dict
virtual_parallel_port_dict = virtual_parallel_port_instance.to_dict()
# create an instance of VirtualParallelPort from a dict
virtual_parallel_port_form_dict = virtual_parallel_port.from_dict(virtual_parallel_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


