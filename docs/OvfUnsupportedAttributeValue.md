# OvfUnsupportedAttributeValue

Used when an OVF descriptor attribute has an unsupported value.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Unsupported attribute value  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_attribute_value import OvfUnsupportedAttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedAttributeValue from a JSON string
ovf_unsupported_attribute_value_instance = OvfUnsupportedAttributeValue.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedAttributeValue.to_json()

# convert the object into a dict
ovf_unsupported_attribute_value_dict = ovf_unsupported_attribute_value_instance.to_dict()
# create an instance of OvfUnsupportedAttributeValue from a dict
ovf_unsupported_attribute_value_form_dict = ovf_unsupported_attribute_value.from_dict(ovf_unsupported_attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


