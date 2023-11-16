# LocalLicenseSource

Deprecated as of vSphere API 4.0, this is not used by the system.  Specify license key data to store locally. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_keys** | **str** | The size of this string is implementation dependent.  It must contain ASCII or ISO Latin-1 characters only.  | 

## Example

```python
from vmware_vi.models.local_license_source import LocalLicenseSource

# TODO update the JSON string below
json = "{}"
# create an instance of LocalLicenseSource from a JSON string
local_license_source_instance = LocalLicenseSource.from_json(json)
# print the JSON string representation of the object
print LocalLicenseSource.to_json()

# convert the object into a dict
local_license_source_dict = local_license_source_instance.to_dict()
# create an instance of LocalLicenseSource from a dict
local_license_source_form_dict = local_license_source.from_dict(local_license_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


