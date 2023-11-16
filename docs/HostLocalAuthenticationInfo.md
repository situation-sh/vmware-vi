# HostLocalAuthenticationInfo

The *HostLocalAuthenticationInfo* data object represents local authentication on the ESX host.  Local authentication is always enabled.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_local_authentication_info import HostLocalAuthenticationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostLocalAuthenticationInfo from a JSON string
host_local_authentication_info_instance = HostLocalAuthenticationInfo.from_json(json)
# print the JSON string representation of the object
print HostLocalAuthenticationInfo.to_json()

# convert the object into a dict
host_local_authentication_info_dict = host_local_authentication_info_instance.to_dict()
# create an instance of HostLocalAuthenticationInfo from a dict
host_local_authentication_info_form_dict = host_local_authentication_info.from_dict(host_local_authentication_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


