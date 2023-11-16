# DvsResourceRuntimeInfo

This class defines the bandwidth reservation information for the vSphere Distributed Switch.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | Capacity: Total Reservation allocated for Virtual Machine Traffic for this switch.  Units in Mbits/s.  ***Since:*** vSphere API 6.0  | [optional] 
**usage** | **int** | usage: Current total usage.  This is the sum of all reservations allocated to *DVSVmVnicNetworkResourcePool* on this switch and the sum of reservation taken by *VirtualEthernetCard* whose backing is not associdated with any *DVSVmVnicNetworkResourcePool*. Units in Mbits/s.  ***Since:*** vSphere API 6.0  | [optional] 
**available** | **int** | Available: Current available resource for reservation (capacity - usage).  Units in Mbits/s.  ***Since:*** vSphere API 6.0  | [optional] 
**allocated_resource** | [**List[DvsVnicAllocatedResource]**](DvsVnicAllocatedResource.md) | The reservation taken by *VirtualEthernetCard* of which the backing is not associdated with any *DVSVmVnicNetworkResourcePool*  ***Since:*** vSphere API 6.0  | [optional] 
**vm_vnic_network_resource_pool_runtime** | [**List[DvsVmVnicNetworkResourcePoolRuntimeInfo]**](DvsVmVnicNetworkResourcePoolRuntimeInfo.md) | The runtime information of *DVSVmVnicNetworkResourcePool*.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_resource_runtime_info import DvsResourceRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DvsResourceRuntimeInfo from a JSON string
dvs_resource_runtime_info_instance = DvsResourceRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print DvsResourceRuntimeInfo.to_json()

# convert the object into a dict
dvs_resource_runtime_info_dict = dvs_resource_runtime_info_instance.to_dict()
# create an instance of DvsResourceRuntimeInfo from a dict
dvs_resource_runtime_info_form_dict = dvs_resource_runtime_info.from_dict(dvs_resource_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


