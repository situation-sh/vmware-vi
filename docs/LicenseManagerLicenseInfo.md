# LicenseManagerLicenseInfo

Encapsulates information about a license  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license_key** | **str** | Key for the license.  E.g. serial number.  ***Since:*** vSphere API 4.0  | 
**edition_key** | **str** | Edition key.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Display name for the license  ***Since:*** vSphere API 4.0  | 
**total** | **int** | Total number of units contain in the license  ***Since:*** vSphere API 4.0  | 
**used** | **int** | Number of units used from this license  ***Since:*** vSphere API 4.0  | [optional] 
**cost_unit** | **str** | The cost unit for this license  ***Since:*** vSphere API 4.0  | 
**properties** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Additional properties associated with this license  ***Since:*** vSphere API 4.0  | [optional] 
**labels** | [**List[KeyValue]**](KeyValue.md) | Key-value lables for this license  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.license_manager_license_info import LicenseManagerLicenseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseManagerLicenseInfo from a JSON string
license_manager_license_info_instance = LicenseManagerLicenseInfo.from_json(json)
# print the JSON string representation of the object
print LicenseManagerLicenseInfo.to_json()

# convert the object into a dict
license_manager_license_info_dict = license_manager_license_info_instance.to_dict()
# create an instance of LicenseManagerLicenseInfo from a dict
license_manager_license_info_form_dict = license_manager_license_info.from_dict(license_manager_license_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


