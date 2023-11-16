# ArrayOfReplicationConfigFault

A boxed array of *ReplicationConfigFault*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationConfigFault]**](ReplicationConfigFault.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_config_fault import ArrayOfReplicationConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationConfigFault from a JSON string
array_of_replication_config_fault_instance = ArrayOfReplicationConfigFault.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationConfigFault.to_json()

# convert the object into a dict
array_of_replication_config_fault_dict = array_of_replication_config_fault_instance.to_dict()
# create an instance of ArrayOfReplicationConfigFault from a dict
array_of_replication_config_fault_form_dict = array_of_replication_config_fault.from_dict(array_of_replication_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


