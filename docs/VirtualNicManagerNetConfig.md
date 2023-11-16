# VirtualNicManagerNetConfig

The NetConfig data object type contains the networking configuration.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_type** | **str** | The NicType of this NetConfig.  ***Since:*** vSphere API 4.0  | 
**multi_select_allowed** | **bool** | Whether multiple nics can be selected for this nicType.  ***Since:*** vSphere API 4.0  | 
**candidate_vnic** | [**List[HostVirtualNic]**](HostVirtualNic.md) | List of VirtualNic objects that may be used.  This will be a subset of the list of VirtualNics in *HostNetworkInfo.vnic*.  ***Since:*** vSphere API 4.0  | [optional] 
**selected_vnic** | [**List[HostVirtualNic]**](HostVirtualNic.md) | List of VirtualNic objects that are selected for use.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_nic_manager_net_config import VirtualNicManagerNetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualNicManagerNetConfig from a JSON string
virtual_nic_manager_net_config_instance = VirtualNicManagerNetConfig.from_json(json)
# print the JSON string representation of the object
print VirtualNicManagerNetConfig.to_json()

# convert the object into a dict
virtual_nic_manager_net_config_dict = virtual_nic_manager_net_config_instance.to_dict()
# create an instance of VirtualNicManagerNetConfig from a dict
virtual_nic_manager_net_config_form_dict = virtual_nic_manager_net_config.from_dict(virtual_nic_manager_net_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


