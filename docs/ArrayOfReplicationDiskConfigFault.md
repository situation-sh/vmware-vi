# ArrayOfReplicationDiskConfigFault

A boxed array of *ReplicationDiskConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationDiskConfigFault]**](ReplicationDiskConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_disk_config_fault import ArrayOfReplicationDiskConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationDiskConfigFault from a JSON string
array_of_replication_disk_config_fault_instance = ArrayOfReplicationDiskConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationDiskConfigFault.to_json()

# convert the object into a dict
array_of_replication_disk_config_fault_dict = array_of_replication_disk_config_fault_instance.to_dict()
# create an instance of ArrayOfReplicationDiskConfigFault from a dict
array_of_replication_disk_config_fault_form_dict = array_of_replication_disk_config_fault.from_dict(array_of_replication_disk_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


