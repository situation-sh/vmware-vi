# ArrayOfVirtualParallelPortOption

A boxed array of *VirtualParallelPortOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualParallelPortOption]**](VirtualParallelPortOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_parallel_port_option import ArrayOfVirtualParallelPortOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualParallelPortOption from a JSON string
array_of_virtual_parallel_port_option_instance = ArrayOfVirtualParallelPortOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualParallelPortOption.to_json()

# convert the object into a dict
array_of_virtual_parallel_port_option_dict = array_of_virtual_parallel_port_option_instance.to_dict()
# create an instance of ArrayOfVirtualParallelPortOption from a dict
array_of_virtual_parallel_port_option_form_dict = array_of_virtual_parallel_port_option.from_dict(array_of_virtual_parallel_port_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


