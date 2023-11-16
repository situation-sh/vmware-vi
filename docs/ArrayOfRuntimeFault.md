# ArrayOfRuntimeFault

A boxed array of *RuntimeFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RuntimeFault]**](RuntimeFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_runtime_fault import ArrayOfRuntimeFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRuntimeFault from a JSON string
array_of_runtime_fault_instance = ArrayOfRuntimeFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfRuntimeFault.to_json()

# convert the object into a dict
array_of_runtime_fault_dict = array_of_runtime_fault_instance.to_dict()
# create an instance of ArrayOfRuntimeFault from a dict
array_of_runtime_fault_form_dict = array_of_runtime_fault.from_dict(array_of_runtime_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


