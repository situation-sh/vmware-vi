# HostPnicNetworkResourceInfo

This data type describes the avaialable capacity for VM traffic on a physical NIC  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pnic_device** | **str** | The physical NIC device  ***Since:*** vSphere API 6.0  | 
**available_bandwidth_for_vm_traffic** | **int** | The total bandwidth available for VM traffic  ***Since:*** vSphere API 6.0  | [optional] 
**unused_bandwidth_for_vm_traffic** | **int** | The unused bandwidth for VM traffic  ***Since:*** vSphere API 6.0  | [optional] 
**placed_virtual_nics** | [**List[HostPlacedVirtualNicIdentifier]**](HostPlacedVirtualNicIdentifier.md) | The connected virtual NICs of powered on Virtual Machines that are placed on this physical NIC  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_pnic_network_resource_info import HostPnicNetworkResourceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostPnicNetworkResourceInfo from a JSON string
host_pnic_network_resource_info_instance = HostPnicNetworkResourceInfo.from_json(json)
# print the JSON string representation of the object
print HostPnicNetworkResourceInfo.to_json()

# convert the object into a dict
host_pnic_network_resource_info_dict = host_pnic_network_resource_info_instance.to_dict()
# create an instance of HostPnicNetworkResourceInfo from a dict
host_pnic_network_resource_info_form_dict = host_pnic_network_resource_info.from_dict(host_pnic_network_resource_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


