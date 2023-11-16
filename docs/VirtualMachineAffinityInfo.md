# VirtualMachineAffinityInfo

Specification of scheduling affinity.  Scheduling affinity is used for explicitly specifying which processors or NUMA nodes may be used by a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affinity_set** | **List[int]** | List of nodes (processors for CPU, NUMA nodes for memory) that may be used by the virtual machine.  If the array is empty when modifying the affinity setting, then any existing affinity is removed.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_affinity_info import VirtualMachineAffinityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineAffinityInfo from a JSON string
virtual_machine_affinity_info_instance = VirtualMachineAffinityInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineAffinityInfo.to_json()

# convert the object into a dict
virtual_machine_affinity_info_dict = virtual_machine_affinity_info_instance.to_dict()
# create an instance of VirtualMachineAffinityInfo from a dict
virtual_machine_affinity_info_form_dict = virtual_machine_affinity_info.from_dict(virtual_machine_affinity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


