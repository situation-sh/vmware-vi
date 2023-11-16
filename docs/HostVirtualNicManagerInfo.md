# HostVirtualNicManagerInfo

This data object type describes VirtualNic host configuration data objects.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**net_config** | [**List[VirtualNicManagerNetConfig]**](VirtualNicManagerNetConfig.md) | List of VirtualNicManager network configuration.  See also *VirtualNicManagerNetConfig*This contains the network configuration for each NicType..  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_nic_manager_info import HostVirtualNicManagerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualNicManagerInfo from a JSON string
host_virtual_nic_manager_info_instance = HostVirtualNicManagerInfo.from_json(json)
# print the JSON string representation of the object
print HostVirtualNicManagerInfo.to_json()

# convert the object into a dict
host_virtual_nic_manager_info_dict = host_virtual_nic_manager_info_instance.to_dict()
# create an instance of HostVirtualNicManagerInfo from a dict
host_virtual_nic_manager_info_form_dict = host_virtual_nic_manager_info.from_dict(host_virtual_nic_manager_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


