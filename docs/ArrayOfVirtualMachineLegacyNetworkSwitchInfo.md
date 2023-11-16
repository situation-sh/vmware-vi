# ArrayOfVirtualMachineLegacyNetworkSwitchInfo

A boxed array of *VirtualMachineLegacyNetworkSwitchInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineLegacyNetworkSwitchInfo]**](VirtualMachineLegacyNetworkSwitchInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_legacy_network_switch_info import ArrayOfVirtualMachineLegacyNetworkSwitchInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineLegacyNetworkSwitchInfo from a JSON string
array_of_virtual_machine_legacy_network_switch_info_instance = ArrayOfVirtualMachineLegacyNetworkSwitchInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineLegacyNetworkSwitchInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_legacy_network_switch_info_dict = array_of_virtual_machine_legacy_network_switch_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineLegacyNetworkSwitchInfo from a dict
array_of_virtual_machine_legacy_network_switch_info_form_dict = array_of_virtual_machine_legacy_network_switch_info.from_dict(array_of_virtual_machine_legacy_network_switch_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


