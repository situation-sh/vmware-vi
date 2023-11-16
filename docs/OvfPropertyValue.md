# OvfPropertyValue

A class used indicate there was a property value error  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_property_value import OvfPropertyValue

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyValue from a JSON string
ovf_property_value_instance = OvfPropertyValue.from_json(json)
# print the JSON string representation of the object
print OvfPropertyValue.to_json()

# convert the object into a dict
ovf_property_value_dict = ovf_property_value_instance.to_dict()
# create an instance of OvfPropertyValue from a dict
ovf_property_value_form_dict = ovf_property_value.from_dict(ovf_property_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


