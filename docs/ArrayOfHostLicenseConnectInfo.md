# ArrayOfHostLicenseConnectInfo

A boxed array of *HostLicenseConnectInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostLicenseConnectInfo]**](HostLicenseConnectInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_license_connect_info import ArrayOfHostLicenseConnectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostLicenseConnectInfo from a JSON string
array_of_host_license_connect_info_instance = ArrayOfHostLicenseConnectInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostLicenseConnectInfo.to_json()

# convert the object into a dict
array_of_host_license_connect_info_dict = array_of_host_license_connect_info_instance.to_dict()
# create an instance of ArrayOfHostLicenseConnectInfo from a dict
array_of_host_license_connect_info_form_dict = array_of_host_license_connect_info.from_dict(array_of_host_license_connect_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


