# ArrayOfNotUserConfigurableProperty

A boxed array of *NotUserConfigurableProperty*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[NotUserConfigurableProperty]**](NotUserConfigurableProperty.md) |  | 

## Example

```python
from vmware_vi.models.array_of_not_user_configurable_property import ArrayOfNotUserConfigurableProperty

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfNotUserConfigurableProperty from a JSON string
array_of_not_user_configurable_property_instance = ArrayOfNotUserConfigurableProperty.from_json(json)
# print the JSON string representation of the object
print ArrayOfNotUserConfigurableProperty.to_json()

# convert the object into a dict
array_of_not_user_configurable_property_dict = array_of_not_user_configurable_property_instance.to_dict()
# create an instance of ArrayOfNotUserConfigurableProperty from a dict
array_of_not_user_configurable_property_form_dict = array_of_not_user_configurable_property.from_dict(array_of_not_user_configurable_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


