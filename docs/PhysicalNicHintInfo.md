# PhysicalNicHintInfo

The NetworkHint data object type is some information about the network to which the physical network adapter is attached. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The physical network adapter device to which this hint applies.  | 
**subnet** | [**List[PhysicalNicIpHint]**](PhysicalNicIpHint.md) | The list of subnets that were detected on this physical network adapter.  | [optional] 
**network** | [**List[PhysicalNicNameHint]**](PhysicalNicNameHint.md) | The list of network names that were detected on this physical network adapter.  | [optional] 
**connected_switch_port** | [**PhysicalNicCdpInfo**](PhysicalNicCdpInfo.md) |  | [optional] 
**lldp_info** | [**LinkLayerDiscoveryProtocolInfo**](LinkLayerDiscoveryProtocolInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.physical_nic_hint_info import PhysicalNicHintInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalNicHintInfo from a JSON string
physical_nic_hint_info_instance = PhysicalNicHintInfo.from_json(json)
# print the JSON string representation of the object
print PhysicalNicHintInfo.to_json()

# convert the object into a dict
physical_nic_hint_info_dict = physical_nic_hint_info_instance.to_dict()
# create an instance of PhysicalNicHintInfo from a dict
physical_nic_hint_info_form_dict = physical_nic_hint_info.from_dict(physical_nic_hint_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


