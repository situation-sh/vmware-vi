# VMwareDVSConfigSpec

This class defines the VMware specific configuration for DistributedVirtualSwitch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pvlan_config_spec** | [**List[VMwareDVSPvlanConfigSpec]**](VMwareDVSPvlanConfigSpec.md) | The PVLAN configuration specification.  A *VMwareDVSPvlanMapEntry* that has the same value for *VMwareDVSPvlanMapEntry.primaryVlanId* and *VMwareDVSPvlanMapEntry.secondaryVlanId* is referred to as a primary PVLAN entry. Otherwise, the *VMwareDVSPvlanMapEntry* is referred to as a secondary PVLAN entry.  The *VMwareDVSPvlanMapEntry.pvlanType* of a primary PVLAN entry must be *promiscuous*. A secondary PVLAN entry can have a *VMwareDVSPvlanMapEntry.pvlanType* of either *community* or *isolated*.  Primary PVLAN entries must be explicitly added. If there is no primary PVLAN entry corresponding to the *VMwareDVSPvlanMapEntry.primaryVlanId* of a secondary PVLAN entry, a fault is thrown.  While deleting a primary PVLAN entry, any associated secondary PVLAN entries must be explicitly deleted.  ***Since:*** vSphere API 4.0  | [optional] 
**vspan_config_spec** | [**List[VMwareDVSVspanConfigSpec]**](VMwareDVSVspanConfigSpec.md) | The Distributed Port Mirroring configuration specification.  The VSPAN sessions in the array cannot be of the same key.  ***Since:*** vSphere API 5.0  | [optional] 
**max_mtu** | **int** | The maximum MTU in the switch.  ***Since:*** vSphere API 4.0  | [optional] 
**link_discovery_protocol_config** | [**LinkDiscoveryProtocolConfig**](LinkDiscoveryProtocolConfig.md) |  | [optional] 
**ipfix_config** | [**VMwareIpfixConfig**](VMwareIpfixConfig.md) |  | [optional] 
**lacp_api_version** | **str** | The Link Aggregation Control Protocol group version in the switch.  See *VMwareDvsLacpApiVersion_enum* for valid values.  ***Since:*** vSphere API 5.5  | [optional] 
**multicast_filtering_mode** | **str** | The Multicast Filtering mode in the switch.  See *VMwareDvsMulticastFilteringMode_enum* for valid values.  ***Since:*** vSphere API 6.0  | [optional] 
**network_offload_spec_id** | **str** | Indicate the ID of NetworkOffloadSpec used in the switch.  Unset it when network offload is not allowed when creating a switch. Use ID \&quot;None\&quot; to change network offload from allowed to not allowed.  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_dvs_config_spec import VMwareDVSConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareDVSConfigSpec from a JSON string
v_mware_dvs_config_spec_instance = VMwareDVSConfigSpec.from_json(json)
# print the JSON string representation of the object
print VMwareDVSConfigSpec.to_json()

# convert the object into a dict
v_mware_dvs_config_spec_dict = v_mware_dvs_config_spec_instance.to_dict()
# create an instance of VMwareDVSConfigSpec from a dict
v_mware_dvs_config_spec_form_dict = v_mware_dvs_config_spec.from_dict(v_mware_dvs_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


