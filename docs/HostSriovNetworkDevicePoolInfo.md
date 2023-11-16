# HostSriovNetworkDevicePoolInfo

Information on networking specific SR-IOV device pools  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_key** | **str** | vSwitch key  ***Since:*** vSphere API 6.5  | [optional] 
**switch_uuid** | **str** | DVS Uuid  ***Since:*** vSphere API 6.5  | [optional] 
**pnic** | [**List[PhysicalNic]**](PhysicalNic.md) | List of SR-IOV enabled physical nics that are backing the portgroup identified by above key  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_sriov_network_device_pool_info import HostSriovNetworkDevicePoolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostSriovNetworkDevicePoolInfo from a JSON string
host_sriov_network_device_pool_info_instance = HostSriovNetworkDevicePoolInfo.from_json(json)
# print the JSON string representation of the object
print HostSriovNetworkDevicePoolInfo.to_json()

# convert the object into a dict
host_sriov_network_device_pool_info_dict = host_sriov_network_device_pool_info_instance.to_dict()
# create an instance of HostSriovNetworkDevicePoolInfo from a dict
host_sriov_network_device_pool_info_form_dict = host_sriov_network_device_pool_info.from_dict(host_sriov_network_device_pool_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


