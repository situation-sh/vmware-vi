# VsanHostConfigInfoNetworkInfo

Host-local VSAN network configuration.  This data object is used both for specifying and retrieving network configuration for a host participating in the VSAN service.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | [**List[VsanHostConfigInfoNetworkInfoPortConfig]**](VsanHostConfigInfoNetworkInfoPortConfig.md) | Set of PortConfig entries for use by the VSAN service, one per \&quot;virtual network\&quot; as used by VSAN.  ***Since:*** vSphere API 5.5  | [optional] 

## Example

```python
from vmware_vi.models.vsan_host_config_info_network_info import VsanHostConfigInfoNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VsanHostConfigInfoNetworkInfo from a JSON string
vsan_host_config_info_network_info_instance = VsanHostConfigInfoNetworkInfo.from_json(json)
# print the JSON string representation of the object
print VsanHostConfigInfoNetworkInfo.to_json()

# convert the object into a dict
vsan_host_config_info_network_info_dict = vsan_host_config_info_network_info_instance.to_dict()
# create an instance of VsanHostConfigInfoNetworkInfo from a dict
vsan_host_config_info_network_info_form_dict = vsan_host_config_info_network_info.from_dict(vsan_host_config_info_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


