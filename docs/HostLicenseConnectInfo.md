# HostLicenseConnectInfo

This data object type describes license information stored on the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | [**LicenseManagerLicenseInfo**](LicenseManagerLicenseInfo.md) |  | 
**evaluation** | [**LicenseManagerEvaluationInfo**](LicenseManagerEvaluationInfo.md) |  | 
**resource** | [**HostLicensableResourceInfo**](HostLicensableResourceInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_license_connect_info import HostLicenseConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostLicenseConnectInfo from a JSON string
host_license_connect_info_instance = HostLicenseConnectInfo.from_json(json)
# print the JSON string representation of the object
print HostLicenseConnectInfo.to_json()

# convert the object into a dict
host_license_connect_info_dict = host_license_connect_info_instance.to_dict()
# create an instance of HostLicenseConnectInfo from a dict
host_license_connect_info_form_dict = host_license_connect_info.from_dict(host_license_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


