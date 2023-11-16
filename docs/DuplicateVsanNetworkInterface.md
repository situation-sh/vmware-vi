# DuplicateVsanNetworkInterface

Fault thrown for cases that duplicate network interface names are incorrectly specified for a VSAN operation.  See also *HostVsanSystem.UpdateVsan_Task*, *ComputeResource.ReconfigureComputeResource_Task*.  ***Since:*** vSphere API 5.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The network interface name found to be duplicated.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.duplicate_vsan_network_interface import DuplicateVsanNetworkInterface

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateVsanNetworkInterface from a JSON string
duplicate_vsan_network_interface_instance = DuplicateVsanNetworkInterface.from_json(json)
# print the JSON string representation of the object
print DuplicateVsanNetworkInterface.to_json()

# convert the object into a dict
duplicate_vsan_network_interface_dict = duplicate_vsan_network_interface_instance.to_dict()
# create an instance of DuplicateVsanNetworkInterface from a dict
duplicate_vsan_network_interface_form_dict = duplicate_vsan_network_interface.from_dict(duplicate_vsan_network_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


