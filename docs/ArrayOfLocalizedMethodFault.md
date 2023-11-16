# ArrayOfLocalizedMethodFault

A boxed array of *LocalizedMethodFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LocalizedMethodFault]**](LocalizedMethodFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_localized_method_fault import ArrayOfLocalizedMethodFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLocalizedMethodFault from a JSON string
array_of_localized_method_fault_instance = ArrayOfLocalizedMethodFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfLocalizedMethodFault.to_json()

# convert the object into a dict
array_of_localized_method_fault_dict = array_of_localized_method_fault_instance.to_dict()
# create an instance of ArrayOfLocalizedMethodFault from a dict
array_of_localized_method_fault_form_dict = array_of_localized_method_fault.from_dict(array_of_localized_method_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


