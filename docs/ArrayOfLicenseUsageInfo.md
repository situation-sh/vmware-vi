# ArrayOfLicenseUsageInfo

A boxed array of *LicenseUsageInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseUsageInfo]**](LicenseUsageInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_usage_info import ArrayOfLicenseUsageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseUsageInfo from a JSON string
array_of_license_usage_info_instance = ArrayOfLicenseUsageInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseUsageInfo.to_json()

# convert the object into a dict
array_of_license_usage_info_dict = array_of_license_usage_info_instance.to_dict()
# create an instance of ArrayOfLicenseUsageInfo from a dict
array_of_license_usage_info_form_dict = array_of_license_usage_info.from_dict(array_of_license_usage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


