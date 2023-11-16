# ArrayOfCustomizationFault

A boxed array of *CustomizationFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[CustomizationFault]**](CustomizationFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_customization_fault import ArrayOfCustomizationFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCustomizationFault from a JSON string
array_of_customization_fault_instance = ArrayOfCustomizationFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfCustomizationFault.to_json()

# convert the object into a dict
array_of_customization_fault_dict = array_of_customization_fault_instance.to_dict()
# create an instance of ArrayOfCustomizationFault from a dict
array_of_customization_fault_form_dict = array_of_customization_fault.from_dict(array_of_customization_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


