# LicenseAvailabilityInfo

Deprecated as of vSphere API 4.0, this is not used by the system.  Describes how many licenses of a particular feature is provided by the licensing source. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | [**LicenseFeatureInfo**](LicenseFeatureInfo.md) |  | 
**total** | **int** | Total number of licenses for this given type that are installed on the source.  | 
**available** | **int** | The number of licenses that have not yet been reserved on the source.  | 

## Example

```python
from vmware_vi.models.license_availability_info import LicenseAvailabilityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseAvailabilityInfo from a JSON string
license_availability_info_instance = LicenseAvailabilityInfo.from_json(json)
# print the JSON string representation of the object
print LicenseAvailabilityInfo.to_json()

# convert the object into a dict
license_availability_info_dict = license_availability_info_instance.to_dict()
# create an instance of LicenseAvailabilityInfo from a dict
license_availability_info_form_dict = license_availability_info.from_dict(license_availability_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


