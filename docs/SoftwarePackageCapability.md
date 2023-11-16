# SoftwarePackageCapability


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**live_install_allowed** | **bool** | True if live installs of this VIB are supported.  ***Since:*** vSphere API 6.5  | [optional] 
**live_remove_allowed** | **bool** | True if live removals of this VIB are supported.  ***Since:*** vSphere API 6.5  | [optional] 
**stateless_ready** | **bool** | True if the package supports host profiles or other technologies that make it suitable for use in conjunction with vSphere Auto Deploy.  ***Since:*** vSphere API 6.5  | [optional] 
**overlay** | **bool** | True if this vib will supplant files from another package at runtime.  When False this prevents two packages from installing the same file.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.software_package_capability import SoftwarePackageCapability

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwarePackageCapability from a JSON string
software_package_capability_instance = SoftwarePackageCapability.from_json(json)
# print the JSON string representation of the object
print SoftwarePackageCapability.to_json()

# convert the object into a dict
software_package_capability_dict = software_package_capability_instance.to_dict()
# create an instance of SoftwarePackageCapability from a dict
software_package_capability_form_dict = software_package_capability.from_dict(software_package_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


