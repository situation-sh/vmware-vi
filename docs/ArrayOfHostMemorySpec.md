# ArrayOfHostMemorySpec

A boxed array of *HostMemorySpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostMemorySpec]**](HostMemorySpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_memory_spec import ArrayOfHostMemorySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostMemorySpec from a JSON string
array_of_host_memory_spec_instance = ArrayOfHostMemorySpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostMemorySpec.to_json()

# convert the object into a dict
array_of_host_memory_spec_dict = array_of_host_memory_spec_instance.to_dict()
# create an instance of ArrayOfHostMemorySpec from a dict
array_of_host_memory_spec_form_dict = array_of_host_memory_spec.from_dict(array_of_host_memory_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


