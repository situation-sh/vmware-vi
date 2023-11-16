# OvfUnsupportedPackage

A common base class to host all the Ovf Lib Unsupported Package faults  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | OVF descriptor linenumber  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.ovf_unsupported_package import OvfUnsupportedPackage

# TODO update the JSON string below
json = "{}"
# create an instance of OvfUnsupportedPackage from a JSON string
ovf_unsupported_package_instance = OvfUnsupportedPackage.from_json(json)
# print the JSON string representation of the object
print OvfUnsupportedPackage.to_json()

# convert the object into a dict
ovf_unsupported_package_dict = ovf_unsupported_package_instance.to_dict()
# create an instance of OvfUnsupportedPackage from a dict
ovf_unsupported_package_form_dict = ovf_unsupported_package.from_dict(ovf_unsupported_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


