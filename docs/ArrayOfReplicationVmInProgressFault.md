# ArrayOfReplicationVmInProgressFault

A boxed array of *ReplicationVmInProgressFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationVmInProgressFault]**](ReplicationVmInProgressFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_vm_in_progress_fault import ArrayOfReplicationVmInProgressFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationVmInProgressFault from a JSON string
array_of_replication_vm_in_progress_fault_instance = ArrayOfReplicationVmInProgressFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationVmInProgressFault.to_json()

# convert the object into a dict
array_of_replication_vm_in_progress_fault_dict = array_of_replication_vm_in_progress_fault_instance.to_dict()
# create an instance of ArrayOfReplicationVmInProgressFault from a dict
array_of_replication_vm_in_progress_fault_form_dict = array_of_replication_vm_in_progress_fault.from_dict(array_of_replication_vm_in_progress_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


