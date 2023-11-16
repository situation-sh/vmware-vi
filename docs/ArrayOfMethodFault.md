# ArrayOfMethodFault

A boxed array of *MethodFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[MethodFault]**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_method_fault import ArrayOfMethodFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfMethodFault from a JSON string
array_of_method_fault_instance = ArrayOfMethodFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfMethodFault.to_json()

# convert the object into a dict
array_of_method_fault_dict = array_of_method_fault_instance.to_dict()
# create an instance of ArrayOfMethodFault from a dict
array_of_method_fault_form_dict = array_of_method_fault.from_dict(array_of_method_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


