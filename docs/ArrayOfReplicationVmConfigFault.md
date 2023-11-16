# ArrayOfReplicationVmConfigFault

A boxed array of *ReplicationVmConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationVmConfigFault]**](ReplicationVmConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_vm_config_fault import ArrayOfReplicationVmConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationVmConfigFault from a JSON string
array_of_replication_vm_config_fault_instance = ArrayOfReplicationVmConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationVmConfigFault.to_json()

# convert the object into a dict
array_of_replication_vm_config_fault_dict = array_of_replication_vm_config_fault_instance.to_dict()
# create an instance of ArrayOfReplicationVmConfigFault from a dict
array_of_replication_vm_config_fault_form_dict = array_of_replication_vm_config_fault.from_dict(array_of_replication_vm_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


