# ArrayOfVirtualParallelPort

A boxed array of *VirtualParallelPort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualParallelPort]**](VirtualParallelPort.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_parallel_port import ArrayOfVirtualParallelPort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualParallelPort from a JSON string
array_of_virtual_parallel_port_instance = ArrayOfVirtualParallelPort.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualParallelPort.to_json()

# convert the object into a dict
array_of_virtual_parallel_port_dict = array_of_virtual_parallel_port_instance.to_dict()
# create an instance of ArrayOfVirtualParallelPort from a dict
array_of_virtual_parallel_port_form_dict = array_of_virtual_parallel_port.from_dict(array_of_virtual_parallel_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


