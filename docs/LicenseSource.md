# LicenseSource

Deprecated as of vSphere API 4.0, this is not used by the system.  This data object type is used to communicate configuration about where to find licenses to use for this system. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.license_source import LicenseSource

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseSource from a JSON string
license_source_instance = LicenseSource.from_json(json)
# print the JSON string representation of the object
print LicenseSource.to_json()

# convert the object into a dict
license_source_dict = license_source_instance.to_dict()
# create an instance of LicenseSource from a dict
license_source_form_dict = license_source.from_dict(license_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


