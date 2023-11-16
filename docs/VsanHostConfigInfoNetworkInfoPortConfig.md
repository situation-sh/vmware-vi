# VsanHostConfigInfoNetworkInfoPortConfig

A PortConfig represents a virtual network adapter and its configuration for use by the VSAN service.  See also *HostVirtualNic*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_config** | [**VsanHostIpConfig**](VsanHostIpConfig.md) |  | [optional] 
**device** | **str** | Device name which identifies the network adapter for this PortConfig.  See also *HostVirtualNic.device*.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.vsan_host_config_info_network_info_port_config import VsanHostConfigInfoNetworkInfoPortConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostConfigInfoNetworkInfoPortConfig from a JSON string
vsan_host_config_info_network_info_port_config_instance = VsanHostConfigInfoNetworkInfoPortConfig.from_json(json)
# print the JSON string representation of the object
print VsanHostConfigInfoNetworkInfoPortConfig.to_json()

# convert the object into a dict
vsan_host_config_info_network_info_port_config_dict = vsan_host_config_info_network_info_port_config_instance.to_dict()
# create an instance of VsanHostConfigInfoNetworkInfoPortConfig from a dict
vsan_host_config_info_network_info_port_config_form_dict = vsan_host_config_info_network_info_port_config.from_dict(vsan_host_config_info_network_info_port_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


