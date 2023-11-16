# OvfUnsupportedAttribute

If the Ovf descriptor have an unsupported attribute.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_name** | **str** | The name of the element with the unsupported attribute  ***Since:*** vSphere API 4.0  | 
**attribute_name** | **str** | The name of the unsupported attribute  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_unsupported_attribute import OvfUnsupportedAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedAttribute from a JSON string
ovf_unsupported_attribute_instance = OvfUnsupportedAttribute.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedAttribute.to_json()

# convert the object into a dict
ovf_unsupported_attribute_dict = ovf_unsupported_attribute_instance.to_dict()
# create an instance of OvfUnsupportedAttribute from a dict
ovf_unsupported_attribute_form_dict = ovf_unsupported_attribute.from_dict(ovf_unsupported_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


