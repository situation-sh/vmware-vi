# OvfAttribute

An OVF descriptor Attribute base class.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element_name** | **str** | Element name where the attribute is defined  ***Since:*** vSphere API 4.0  | 
**attribute_name** | **str** | Attribute name  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_attribute import OvfAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of OvfAttribute from a JSON string
ovf_attribute_instance = OvfAttribute.from_json(json)
# print the JSON string representation of the object
print OvfAttribute.to_json()

# convert the object into a dict
ovf_attribute_dict = ovf_attribute_instance.to_dict()
# create an instance of OvfAttribute from a dict
ovf_attribute_form_dict = ovf_attribute.from_dict(ovf_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


