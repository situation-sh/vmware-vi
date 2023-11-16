# ReplicationVmInProgressFault

A ReplicationVmInProgressFault is thrown when a replication operation failed to perform on a *VirtualMachine* because the VM is in the middle of another replication activity.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_activity** | **str** | The requsted activity for VM replication  ***Since:*** vSphere API 6.0  | 
**in_progress_activity** | **str** | The in-progress activity for VM replication  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.replication_vm_in_progress_fault import ReplicationVmInProgressFault

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationVmInProgressFault from a JSON string
replication_vm_in_progress_fault_instance = ReplicationVmInProgressFault.from_json(json)
# print the JSON string representation of the object
print ReplicationVmInProgressFault.to_json()

# convert the object into a dict
replication_vm_in_progress_fault_dict = replication_vm_in_progress_fault_instance.to_dict()
# create an instance of ReplicationVmInProgressFault from a dict
replication_vm_in_progress_fault_form_dict = replication_vm_in_progress_fault.from_dict(replication_vm_in_progress_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


