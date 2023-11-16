# VirtualMachineNetworkShaperInfo

Network traffic shaping specification.  Traffic shaping is used to configure the network utilization characteristics of a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is the shaper enabled?  | [optional] 
**peak_bps** | **int** | Peak bandwidth, in bits per second.  | [optional] 
**average_bps** | **int** | Average bandwidth, in bits per second.  | [optional] 
**burst_size** | **int** | Burst size, in bytes.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_network_shaper_info import VirtualMachineNetworkShaperInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineNetworkShaperInfo from a JSON string
virtual_machine_network_shaper_info_instance = VirtualMachineNetworkShaperInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineNetworkShaperInfo.to_json()

# convert the object into a dict
virtual_machine_network_shaper_info_dict = virtual_machine_network_shaper_info_instance.to_dict()
# create an instance of VirtualMachineNetworkShaperInfo from a dict
virtual_machine_network_shaper_info_form_dict = virtual_machine_network_shaper_info.from_dict(virtual_machine_network_shaper_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


