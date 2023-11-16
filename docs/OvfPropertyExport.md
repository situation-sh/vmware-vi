# OvfPropertyExport

VIM property type that can not be converted to OVF  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | VIM type  ***Since:*** vSphere API 4.0  | 
**value** | **str** | VIM value  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_property_export import OvfPropertyExport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyExport from a JSON string
ovf_property_export_instance = OvfPropertyExport.from_json(json)
# print the JSON string representation of the object
print OvfPropertyExport.to_json()

# convert the object into a dict
ovf_property_export_dict = ovf_property_export_instance.to_dict()
# create an instance of OvfPropertyExport from a dict
ovf_property_export_form_dict = ovf_property_export.from_dict(ovf_property_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


