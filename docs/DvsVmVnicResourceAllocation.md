# DvsVmVnicResourceAllocation

Resource allocation information for a virtual NIC network resource pool.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_quota** | **int** | Quota for the total amount of virtual machine nic reservation in this pool.  Unit in Mbits/sec.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.dvs_vm_vnic_resource_allocation import DvsVmVnicResourceAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of DvsVmVnicResourceAllocation from a JSON string
dvs_vm_vnic_resource_allocation_instance = DvsVmVnicResourceAllocation.from_json(json)
# print the JSON string representation of the object
print DvsVmVnicResourceAllocation.to_json()

# convert the object into a dict
dvs_vm_vnic_resource_allocation_dict = dvs_vm_vnic_resource_allocation_instance.to_dict()
# create an instance of DvsVmVnicResourceAllocation from a dict
dvs_vm_vnic_resource_allocation_form_dict = dvs_vm_vnic_resource_allocation.from_dict(dvs_vm_vnic_resource_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


