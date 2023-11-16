# VirtualMachineLegacyNetworkSwitchInfo

The LegacyNetworkSwitchInfo data object type contains information about the legacy network switches available on the host. - VMware Server - Options available for the \"custom\" NetworkBackingType. - ESX Server - The \"esxnet\" NetworkBackingType. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the network switch.  | 

## Example

```python
from vmware_vi.models.virtual_machine_legacy_network_switch_info import VirtualMachineLegacyNetworkSwitchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineLegacyNetworkSwitchInfo from a JSON string
virtual_machine_legacy_network_switch_info_instance = VirtualMachineLegacyNetworkSwitchInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineLegacyNetworkSwitchInfo.to_json()

# convert the object into a dict
virtual_machine_legacy_network_switch_info_dict = virtual_machine_legacy_network_switch_info_instance.to_dict()
# create an instance of VirtualMachineLegacyNetworkSwitchInfo from a dict
virtual_machine_legacy_network_switch_info_form_dict = virtual_machine_legacy_network_switch_info.from_dict(virtual_machine_legacy_network_switch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


