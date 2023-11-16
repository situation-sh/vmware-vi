# DvsVmVnicNetworkResourcePoolRuntimeInfo

This class defines the runtime information for the virtual NIC network resource pool  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the virtual NIC network resource pool  ***Since:*** vSphere API 6.0  | 
**name** | **str** | The name of the virtual NIC network resource pool  ***Since:*** vSphere API 6.0  | [optional] 
**capacity** | **int** | Capacity: Reservation allocated for this Network Resource Pool.  Units in Mbits/s.  ***Since:*** vSphere API 6.0  | [optional] 
**usage** | **int** | usage: Reservation taken by all *VirtualEthernetCard* for which the backing is associdated with this *DVSVmVnicNetworkResourcePool*.  Units in Mbits/s.  ***Since:*** vSphere API 6.0  | [optional] 
**available** | **int** | Available: Current available resource for reservation (capacity - usage).  Units in Mbits/s.  ***Since:*** vSphere API 6.0  | [optional] 
**status** | **str** | The status of the virtual NIC network resource pool See *ManagedEntityStatus_enum* for possible values  *red* indicates that the reservations used by all the virtual network adapters belonging to this resource pool exceeds the total reservation quota allocated to the resource pool. This can happen due to failure of one or more uplink or if the user bypasses VirtualCenter and powers on VMs directly on host. The reservation of one or more virtual network adapters cannot be guaranteed and corrective action needs to be taken by the user.  *green* indicates that the resource pool is in good state. The reservations for all virtual network adapters can be fulfilled.  ***Since:*** vSphere API 6.0  | 
**allocated_resource** | [**List[DvsVnicAllocatedResource]**](DvsVnicAllocatedResource.md) | The virtual network adapaters that are currently associated with the resource pool  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_vm_vnic_network_resource_pool_runtime_info import DvsVmVnicNetworkResourcePoolRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DvsVmVnicNetworkResourcePoolRuntimeInfo from a JSON string
dvs_vm_vnic_network_resource_pool_runtime_info_instance = DvsVmVnicNetworkResourcePoolRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print DvsVmVnicNetworkResourcePoolRuntimeInfo.to_json()

# convert the object into a dict
dvs_vm_vnic_network_resource_pool_runtime_info_dict = dvs_vm_vnic_network_resource_pool_runtime_info_instance.to_dict()
# create an instance of DvsVmVnicNetworkResourcePoolRuntimeInfo from a dict
dvs_vm_vnic_network_resource_pool_runtime_info_form_dict = dvs_vm_vnic_network_resource_pool_runtime_info.from_dict(dvs_vm_vnic_network_resource_pool_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


