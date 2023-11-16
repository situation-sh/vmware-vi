# NotUserConfigurableProperty

The property value cannot be changed since it is not user configurable.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.not_user_configurable_property import NotUserConfigurableProperty

# TODO update the JSON string below
json = "{}"
# create an instance of NotUserConfigurableProperty from a JSON string
not_user_configurable_property_instance = NotUserConfigurableProperty.from_json(json)
# print the JSON string representation of the object
print NotUserConfigurableProperty.to_json()

# convert the object into a dict
not_user_configurable_property_dict = not_user_configurable_property_instance.to_dict()
# create an instance of NotUserConfigurableProperty from a dict
not_user_configurable_property_form_dict = not_user_configurable_property.from_dict(not_user_configurable_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


