# VirtualMachineNetworkInfo

NetworkInfo describes a network that a device backing can attached to. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | [**NetworkSummary**](NetworkSummary.md) |  | 
**vswitch** | **str** | Key of parent vSwitch of the network  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_network_info import VirtualMachineNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineNetworkInfo from a JSON string
virtual_machine_network_info_instance = VirtualMachineNetworkInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineNetworkInfo.to_json()

# convert the object into a dict
virtual_machine_network_info_dict = virtual_machine_network_info_instance.to_dict()
# create an instance of VirtualMachineNetworkInfo from a dict
virtual_machine_network_info_form_dict = virtual_machine_network_info.from_dict(virtual_machine_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


