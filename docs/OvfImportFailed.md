# OvfImportFailed

This fault is used if we fail to deploy an OVF package.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_import_failed import OvfImportFailed

# TODO update the JSON string below
json = "{}"
# create an instance of OvfImportFailed from a JSON string
ovf_import_failed_instance = OvfImportFailed.from_json(json)
# print the JSON string representation of the object
print OvfImportFailed.to_json()

# convert the object into a dict
ovf_import_failed_dict = ovf_import_failed_instance.to_dict()
# create an instance of OvfImportFailed from a dict
ovf_import_failed_form_dict = ovf_import_failed.from_dict(ovf_import_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


