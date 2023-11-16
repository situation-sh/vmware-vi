# OvfPropertyType

A class used to indicate there was a property type error  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_property_type import OvfPropertyType

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyType from a JSON string
ovf_property_type_instance = OvfPropertyType.from_json(json)
# print the JSON string representation of the object
print OvfPropertyType.to_json()

# convert the object into a dict
ovf_property_type_dict = ovf_property_type_instance.to_dict()
# create an instance of OvfPropertyType from a dict
ovf_property_type_form_dict = ovf_property_type.from_dict(ovf_property_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


