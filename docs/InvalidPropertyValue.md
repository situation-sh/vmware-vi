# InvalidPropertyValue

The value of the property is not valid given the type of the property.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.invalid_property_value import InvalidPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidPropertyValue from a JSON string
invalid_property_value_instance = InvalidPropertyValue.from_json(json)
# print the JSON string representation of the object
print InvalidPropertyValue.to_json()

# convert the object into a dict
invalid_property_value_dict = invalid_property_value_instance.to_dict()
# create an instance of InvalidPropertyValue from a dict
invalid_property_value_form_dict = invalid_property_value.from_dict(invalid_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


