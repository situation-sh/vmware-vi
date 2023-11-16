# CustomizationOptions

Base object type for optional operations supported by the customization process. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_options import CustomizationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationOptions from a JSON string
customization_options_instance = CustomizationOptions.from_json(json)
# print the JSON string representation of the object
print CustomizationOptions.to_json()

# convert the object into a dict
customization_options_dict = customization_options_instance.to_dict()
# create an instance of CustomizationOptions from a dict
customization_options_form_dict = customization_options.from_dict(customization_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


