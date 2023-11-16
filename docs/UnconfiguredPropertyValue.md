# UnconfiguredPropertyValue

The property value has not been configured by the user, so the application cannot be started.  This is thrown if a property value is the empty string and the types does not allow it. For example, for an integer type or a string where the minimum length is 1, and so forth.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.unconfigured_property_value import UnconfiguredPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of UnconfiguredPropertyValue from a JSON string
unconfigured_property_value_instance = UnconfiguredPropertyValue.from_json(json)
# print the JSON string representation of the object
print UnconfiguredPropertyValue.to_json()

# convert the object into a dict
unconfigured_property_value_dict = unconfigured_property_value_instance.to_dict()
# create an instance of UnconfiguredPropertyValue from a dict
unconfigured_property_value_form_dict = unconfigured_property_value.from_dict(unconfigured_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


