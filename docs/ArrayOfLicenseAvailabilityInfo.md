# ArrayOfLicenseAvailabilityInfo

A boxed array of *LicenseAvailabilityInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LicenseAvailabilityInfo]**](LicenseAvailabilityInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_license_availability_info import ArrayOfLicenseAvailabilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLicenseAvailabilityInfo from a JSON string
array_of_license_availability_info_instance = ArrayOfLicenseAvailabilityInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfLicenseAvailabilityInfo.to_json()

# convert the object into a dict
array_of_license_availability_info_dict = array_of_license_availability_info_instance.to_dict()
# create an instance of ArrayOfLicenseAvailabilityInfo from a dict
array_of_license_availability_info_form_dict = array_of_license_availability_info.from_dict(array_of_license_availability_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


