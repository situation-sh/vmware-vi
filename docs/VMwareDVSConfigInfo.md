# VMwareDVSConfigInfo

This class defines the VMware specific configuration for DistributedVirtualSwitch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vspan_session** | [**List[VMwareVspanSession]**](VMwareVspanSession.md) | The Distributed Port Mirroring sessions in the switch.  ***Since:*** vSphere API 5.0  | [optional] 
**pvlan_config** | [**List[VMwareDVSPvlanMapEntry]**](VMwareDVSPvlanMapEntry.md) | The PVLAN configured in the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**max_mtu** | **int** | The maximum MTU in the switch.  ***Since:*** vSphere API 4.0  | 
**link_discovery_protocol_config** | [**LinkDiscoveryProtocolConfig**](LinkDiscoveryProtocolConfig.md) |  | [optional] 
**ipfix_config** | [**VMwareIpfixConfig**](VMwareIpfixConfig.md) |  | [optional] 
**lacp_group_config** | [**List[VMwareDvsLacpGroupConfig]**](VMwareDvsLacpGroupConfig.md) | The Link Aggregation Control Protocol groups in the switch.  ***Since:*** vSphere API 5.5  | [optional] 
**lacp_api_version** | **str** | The Link Aggregation Control Protocol group version in the switch.  See *VMwareDvsLacpApiVersion_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 
**multicast_filtering_mode** | **str** | The Multicast Filtering mode in the switch.  See *VMwareDvsMulticastFilteringMode_enum* for valid values.  ***Since:*** vSphere API 6.0  | [optional] 
**network_offload_spec_id** | **str** | Indicate the ID of NetworkOffloadSpec used in the switch.  ID \&quot;None\&quot; means that network offload is not allowed in the switch.  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_config_info import VMwareDVSConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSConfigInfo from a JSON string
v_mware_dvs_config_info_instance = VMwareDVSConfigInfo.from_json(json)
# print the JSON string representation of the object
print VMwareDVSConfigInfo.to_json()

# convert the object into a dict
v_mware_dvs_config_info_dict = v_mware_dvs_config_info_instance.to_dict()
# create an instance of VMwareDVSConfigInfo from a dict
v_mware_dvs_config_info_form_dict = v_mware_dvs_config_info.from_dict(v_mware_dvs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


