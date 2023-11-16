# OvfPropertyQualifierIgnored

Indicate that the was qualifier was ignored  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**qualifier** | **str** | qualifiers  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_property_qualifier_ignored import OvfPropertyQualifierIgnored

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyQualifierIgnored from a JSON string
ovf_property_qualifier_ignored_instance = OvfPropertyQualifierIgnored.from_json(json)
# print the JSON string representation of the object
print OvfPropertyQualifierIgnored.to_json()

# convert the object into a dict
ovf_property_qualifier_ignored_dict = ovf_property_qualifier_ignored_instance.to_dict()
# create an instance of OvfPropertyQualifierIgnored from a dict
ovf_property_qualifier_ignored_form_dict = ovf_property_qualifier_ignored.from_dict(ovf_property_qualifier_ignored_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


