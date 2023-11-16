# CustomizationUnknownName

Indicates that the name is not specified in advance.  The client should prompt the user for the value to complete the specification. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_unknown_name import CustomizationUnknownName

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationUnknownName from a JSON string
customization_unknown_name_instance = CustomizationUnknownName.from_json(json)
# print the JSON string representation of the object
print CustomizationUnknownName.to_json()

# convert the object into a dict
customization_unknown_name_dict = customization_unknown_name_instance.to_dict()
# create an instance of CustomizationUnknownName from a dict
customization_unknown_name_form_dict = customization_unknown_name.from_dict(customization_unknown_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


