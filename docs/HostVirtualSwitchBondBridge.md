# HostVirtualSwitchBondBridge

This data object type describes a bridge that provides network adapter teaming capabilities. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_device** | **List[str]** | The list of keys of the physical network adapters to be bridged.  | 
**beacon** | [**HostVirtualSwitchBeaconConfig**](HostVirtualSwitchBeaconConfig.md) |  | [optional] 
**link_discovery_protocol_config** | [**LinkDiscoveryProtocolConfig**](LinkDiscoveryProtocolConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_virtual_switch_bond_bridge import HostVirtualSwitchBondBridge

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchBondBridge from a JSON string
host_virtual_switch_bond_bridge_instance = HostVirtualSwitchBondBridge.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchBondBridge.to_json()

# convert the object into a dict
host_virtual_switch_bond_bridge_dict = host_virtual_switch_bond_bridge_instance.to_dict()
# create an instance of HostVirtualSwitchBondBridge from a dict
host_virtual_switch_bond_bridge_form_dict = host_virtual_switch_bond_bridge.from_dict(host_virtual_switch_bond_bridge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


