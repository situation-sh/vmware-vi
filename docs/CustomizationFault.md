# CustomizationFault

Base for exceptions that can be thrown from the customizer. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_fault import CustomizationFault

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationFault from a JSON string
customization_fault_instance = CustomizationFault.from_json(json)
# print the JSON string representation of the object
print CustomizationFault.to_json()

# convert the object into a dict
customization_fault_dict = customization_fault_instance.to_dict()
# create an instance of CustomizationFault from a dict
customization_fault_form_dict = customization_fault.from_dict(customization_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


