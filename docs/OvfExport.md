# OvfExport

A common base class to host all the Ovf Lib Export Exceptions.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_export import OvfExport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfExport from a JSON string
ovf_export_instance = OvfExport.from_json(json)
# print the JSON string representation of the object
print OvfExport.to_json()

# convert the object into a dict
ovf_export_dict = ovf_export_instance.to_dict()
# create an instance of OvfExport from a dict
ovf_export_form_dict = ovf_export.from_dict(ovf_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


