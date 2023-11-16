# HostSriovDevicePoolInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 

## Example

```python
from vmware_vi.models.host_sriov_device_pool_info import HostSriovDevicePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSriovDevicePoolInfo from a JSON string
host_sriov_device_pool_info_instance = HostSriovDevicePoolInfo.from_json(json)
# print the JSON string representation of the object
print HostSriovDevicePoolInfo.to_json()

# convert the object into a dict
host_sriov_device_pool_info_dict = host_sriov_device_pool_info_instance.to_dict()
# create an instance of HostSriovDevicePoolInfo from a dict
host_sriov_device_pool_info_form_dict = host_sriov_device_pool_info.from_dict(host_sriov_device_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


