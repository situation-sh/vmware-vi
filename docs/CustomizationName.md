# CustomizationName

A base object type for a virtual machine name that can be either fixed or auto-generated. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_name import CustomizationName

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationName from a JSON string
customization_name_instance = CustomizationName.from_json(json)
# print the JSON string representation of the object
print CustomizationName.to_json()

# convert the object into a dict
customization_name_dict = customization_name_instance.to_dict()
# create an instance of CustomizationName from a dict
customization_name_form_dict = customization_name.from_dict(customization_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


