# ReplicationVmConfigFault

A ReplicationVmConfigFault is thrown when there is an issue with configuring VM-wide replication properties.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  One of the above *ReplicationVmConfigFaultReasonForFault_enum*.  ***Since:*** vSphere API 5.0  | [optional] 
**vm_ref** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.replication_vm_config_fault import ReplicationVmConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationVmConfigFault from a JSON string
replication_vm_config_fault_instance = ReplicationVmConfigFault.from_json(json)
# print the JSON string representation of the object
print ReplicationVmConfigFault.to_json()

# convert the object into a dict
replication_vm_config_fault_dict = replication_vm_config_fault_instance.to_dict()
# create an instance of ReplicationVmConfigFault from a dict
replication_vm_config_fault_form_dict = replication_vm_config_fault.from_dict(replication_vm_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


