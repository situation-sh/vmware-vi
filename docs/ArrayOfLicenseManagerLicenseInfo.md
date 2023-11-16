# ArrayOfLicenseManagerLicenseInfo

A boxed array of *LicenseManagerLicenseInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseManagerLicenseInfo]**](LicenseManagerLicenseInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_manager_license_info import ArrayOfLicenseManagerLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseManagerLicenseInfo from a JSON string
array_of_license_manager_license_info_instance = ArrayOfLicenseManagerLicenseInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseManagerLicenseInfo.to_json()

# convert the object into a dict
array_of_license_manager_license_info_dict = array_of_license_manager_license_info_instance.to_dict()
# create an instance of ArrayOfLicenseManagerLicenseInfo from a dict
array_of_license_manager_license_info_form_dict = array_of_license_manager_license_info.from_dict(array_of_license_manager_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


