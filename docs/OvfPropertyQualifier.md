# OvfPropertyQualifier

A class used to indicate there was a property qualifier error  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qualifier** | **str** | qualifiers  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_property_qualifier import OvfPropertyQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyQualifier from a JSON string
ovf_property_qualifier_instance = OvfPropertyQualifier.from_json(json)
# print the JSON string representation of the object
print OvfPropertyQualifier.to_json()

# convert the object into a dict
ovf_property_qualifier_dict = ovf_property_qualifier_instance.to_dict()
# create an instance of OvfPropertyQualifier from a dict
ovf_property_qualifier_form_dict = ovf_property_qualifier.from_dict(ovf_property_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


