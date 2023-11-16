# ArrayOfUnexpectedCustomizationFault

A boxed array of *UnexpectedCustomizationFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UnexpectedCustomizationFault]**](UnexpectedCustomizationFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_unexpected_customization_fault import ArrayOfUnexpectedCustomizationFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUnexpectedCustomizationFault from a JSON string
array_of_unexpected_customization_fault_instance = ArrayOfUnexpectedCustomizationFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfUnexpectedCustomizationFault.to_json()

# convert the object into a dict
array_of_unexpected_customization_fault_dict = array_of_unexpected_customization_fault_instance.to_dict()
# create an instance of ArrayOfUnexpectedCustomizationFault from a dict
array_of_unexpected_customization_fault_form_dict = array_of_unexpected_customization_fault.from_dict(array_of_unexpected_customization_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


