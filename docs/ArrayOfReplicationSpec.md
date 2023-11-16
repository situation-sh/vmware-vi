# ArrayOfReplicationSpec

A boxed array of *ReplicationSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationSpec]**](ReplicationSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_spec import ArrayOfReplicationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationSpec from a JSON string
array_of_replication_spec_instance = ArrayOfReplicationSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationSpec.to_json()

# convert the object into a dict
array_of_replication_spec_dict = array_of_replication_spec_instance.to_dict()
# create an instance of ArrayOfReplicationSpec from a dict
array_of_replication_spec_form_dict = array_of_replication_spec.from_dict(array_of_replication_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


