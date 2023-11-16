# OvfInvalidPackage

Base fault class for all Invalid OVF package faults.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | XML OVF descriptor line numbers  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_invalid_package import OvfInvalidPackage

# TODO update the JSON string below
json = "{}"
# create an instance of OvfInvalidPackage from a JSON string
ovf_invalid_package_instance = OvfInvalidPackage.from_json(json)
# print the JSON string representation of the object
print OvfInvalidPackage.to_json()

# convert the object into a dict
ovf_invalid_package_dict = ovf_invalid_package_instance.to_dict()
# create an instance of OvfInvalidPackage from a dict
ovf_invalid_package_form_dict = ovf_invalid_package.from_dict(ovf_invalid_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


