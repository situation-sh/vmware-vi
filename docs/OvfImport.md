# OvfImport

A common base class for errors that can happen during Import and that is not due to an invalid package (OvfInvalidPackage).  These are typically issued as warnings.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.ovf_import import OvfImport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfImport from a JSON string
ovf_import_instance = OvfImport.from_json(json)
# print the JSON string representation of the object
print OvfImport.to_json()

# convert the object into a dict
ovf_import_dict = ovf_import_instance.to_dict()
# create an instance of OvfImport from a dict
ovf_import_form_dict = ovf_import.from_dict(ovf_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


