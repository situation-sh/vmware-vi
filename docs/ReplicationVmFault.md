# ReplicationVmFault

A ReplicationVmFault is thrown when there is an issue with an operation performed on a replicated *VirtualMachine*  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  One of the above.  ***Since:*** vSphere API 5.0  | 
**state** | **str** | The current *ReplicationVmState_enum* of the *VirtualMachine*  ***Since:*** vSphere API 5.0  | [optional] 
**instance_id** | **str** | The name of the instance currently being created.  ***Since:*** vSphere API 5.0  | [optional] 
**vm** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.replication_vm_fault import ReplicationVmFault

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationVmFault from a JSON string
replication_vm_fault_instance = ReplicationVmFault.from_json(json)
# print the JSON string representation of the object
print ReplicationVmFault.to_json()

# convert the object into a dict
replication_vm_fault_dict = replication_vm_fault_instance.to_dict()
# create an instance of ReplicationVmFault from a dict
replication_vm_fault_form_dict = replication_vm_fault.from_dict(replication_vm_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


