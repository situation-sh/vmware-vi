# ArrayOfUnconfiguredPropertyValue

A boxed array of *UnconfiguredPropertyValue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UnconfiguredPropertyValue]**](UnconfiguredPropertyValue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_unconfigured_property_value import ArrayOfUnconfiguredPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUnconfiguredPropertyValue from a JSON string
array_of_unconfigured_property_value_instance = ArrayOfUnconfiguredPropertyValue.from_json(json)
# print the JSON string representation of the object
print ArrayOfUnconfiguredPropertyValue.to_json()

# convert the object into a dict
array_of_unconfigured_property_value_dict = array_of_unconfigured_property_value_instance.to_dict()
# create an instance of ArrayOfUnconfiguredPropertyValue from a dict
array_of_unconfigured_property_value_form_dict = array_of_unconfigured_property_value.from_dict(array_of_unconfigured_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


