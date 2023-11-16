# ArrayOfReplicationGroupId

A boxed array of *ReplicationGroupId*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationGroupId]**](ReplicationGroupId.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_group_id import ArrayOfReplicationGroupId

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationGroupId from a JSON string
array_of_replication_group_id_instance = ArrayOfReplicationGroupId.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationGroupId.to_json()

# convert the object into a dict
array_of_replication_group_id_dict = array_of_replication_group_id_instance.to_dict()
# create an instance of ArrayOfReplicationGroupId from a dict
array_of_replication_group_id_form_dict = array_of_replication_group_id.from_dict(array_of_replication_group_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


