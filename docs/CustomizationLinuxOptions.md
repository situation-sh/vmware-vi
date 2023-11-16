# CustomizationLinuxOptions

Base object type for optional operations supported by the customization process for Linux. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_linux_options import CustomizationLinuxOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationLinuxOptions from a JSON string
customization_linux_options_instance = CustomizationLinuxOptions.from_json(json)
# print the JSON string representation of the object
print CustomizationLinuxOptions.to_json()

# convert the object into a dict
customization_linux_options_dict = customization_linux_options_instance.to_dict()
# create an instance of CustomizationLinuxOptions from a dict
customization_linux_options_form_dict = customization_linux_options.from_dict(customization_linux_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


