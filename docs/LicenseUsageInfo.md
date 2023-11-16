# LicenseUsageInfo

Deprecated as of vSphere API 4.0, this is not used by the system.  Contains source information, licensed features, and usage. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**LicenseSource**](LicenseSource.md) |  | 
**source_available** | **bool** | Returns whether or not the source is currently available.  See also *LicenseManager.sourceAvailable*.  | 
**reservation_info** | [**List[LicenseReservationInfo]**](LicenseReservationInfo.md) | A list of feature reservations.  | [optional] 
**feature_info** | [**List[LicenseFeatureInfo]**](LicenseFeatureInfo.md) | Includes all the features that are referenced in the reservation array.  | [optional] 

## Example

```python
from vmware_vi.models.license_usage_info import LicenseUsageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseUsageInfo from a JSON string
license_usage_info_instance = LicenseUsageInfo.from_json(json)
# print the JSON string representation of the object
print LicenseUsageInfo.to_json()

# convert the object into a dict
license_usage_info_dict = license_usage_info_instance.to_dict()
# create an instance of LicenseUsageInfo from a dict
license_usage_info_form_dict = license_usage_info.from_dict(license_usage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


