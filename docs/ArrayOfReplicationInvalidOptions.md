# ArrayOfReplicationInvalidOptions

A boxed array of *ReplicationInvalidOptions*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationInvalidOptions]**](ReplicationInvalidOptions.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_invalid_options import ArrayOfReplicationInvalidOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationInvalidOptions from a JSON string
array_of_replication_invalid_options_instance = ArrayOfReplicationInvalidOptions.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationInvalidOptions.to_json()

# convert the object into a dict
array_of_replication_invalid_options_dict = array_of_replication_invalid_options_instance.to_dict()
# create an instance of ArrayOfReplicationInvalidOptions from a dict
array_of_replication_invalid_options_form_dict = array_of_replication_invalid_options.from_dict(array_of_replication_invalid_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


