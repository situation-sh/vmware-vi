# ArrayOfInsufficientCpuResourcesFault

A boxed array of *InsufficientCpuResourcesFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InsufficientCpuResourcesFault]**](InsufficientCpuResourcesFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_insufficient_cpu_resources_fault import ArrayOfInsufficientCpuResourcesFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInsufficientCpuResourcesFault from a JSON string
array_of_insufficient_cpu_resources_fault_instance = ArrayOfInsufficientCpuResourcesFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfInsufficientCpuResourcesFault.to_json()

# convert the object into a dict
array_of_insufficient_cpu_resources_fault_dict = array_of_insufficient_cpu_resources_fault_instance.to_dict()
# create an instance of ArrayOfInsufficientCpuResourcesFault from a dict
array_of_insufficient_cpu_resources_fault_form_dict = array_of_insufficient_cpu_resources_fault.from_dict(array_of_insufficient_cpu_resources_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


