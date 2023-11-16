# ArrayOfDvsVmVnicResourceAllocation

A boxed array of *DvsVmVnicResourceAllocation*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[DvsVmVnicResourceAllocation]**](DvsVmVnicResourceAllocation.md) |  | 

## Example

```python
from vmware_vi.models.array_of_dvs_vm_vnic_resource_allocation import ArrayOfDvsVmVnicResourceAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDvsVmVnicResourceAllocation from a JSON string
array_of_dvs_vm_vnic_resource_allocation_instance = ArrayOfDvsVmVnicResourceAllocation.from_json(json)
# print the JSON string representation of the object
print ArrayOfDvsVmVnicResourceAllocation.to_json()

# convert the object into a dict
array_of_dvs_vm_vnic_resource_allocation_dict = array_of_dvs_vm_vnic_resource_allocation_instance.to_dict()
# create an instance of ArrayOfDvsVmVnicResourceAllocation from a dict
array_of_dvs_vm_vnic_resource_allocation_form_dict = array_of_dvs_vm_vnic_resource_allocation.from_dict(array_of_dvs_vm_vnic_resource_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


