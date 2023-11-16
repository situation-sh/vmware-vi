# ArrayOfReplicationVmProgressInfo

A boxed array of *ReplicationVmProgressInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationVmProgressInfo]**](ReplicationVmProgressInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_vm_progress_info import ArrayOfReplicationVmProgressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationVmProgressInfo from a JSON string
array_of_replication_vm_progress_info_instance = ArrayOfReplicationVmProgressInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationVmProgressInfo.to_json()

# convert the object into a dict
array_of_replication_vm_progress_info_dict = array_of_replication_vm_progress_info_instance.to_dict()
# create an instance of ArrayOfReplicationVmProgressInfo from a dict
array_of_replication_vm_progress_info_form_dict = array_of_replication_vm_progress_info.from_dict(array_of_replication_vm_progress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


