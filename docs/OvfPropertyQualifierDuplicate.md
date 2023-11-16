# OvfPropertyQualifierDuplicate

Indicate that a property qualifier was duplicated.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qualifier** | **str** | qualifiers  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_property_qualifier_duplicate import OvfPropertyQualifierDuplicate

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyQualifierDuplicate from a JSON string
ovf_property_qualifier_duplicate_instance = OvfPropertyQualifierDuplicate.from_json(json)
# print the JSON string representation of the object
print OvfPropertyQualifierDuplicate.to_json()

# convert the object into a dict
ovf_property_qualifier_duplicate_dict = ovf_property_qualifier_duplicate_instance.to_dict()
# create an instance of OvfPropertyQualifierDuplicate from a dict
ovf_property_qualifier_duplicate_form_dict = ovf_property_qualifier_duplicate.from_dict(ovf_property_qualifier_duplicate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


