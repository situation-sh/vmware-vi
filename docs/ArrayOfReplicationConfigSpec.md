# ArrayOfReplicationConfigSpec

A boxed array of *ReplicationConfigSpec*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ReplicationConfigSpec]**](ReplicationConfigSpec.md) |  | 

## Example

```python
from vmware_vi.models.array_of_replication_config_spec import ArrayOfReplicationConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfReplicationConfigSpec from a JSON string
array_of_replication_config_spec_instance = ArrayOfReplicationConfigSpec.from_json(json)
# print the JSON string representation of the object
print ArrayOfReplicationConfigSpec.to_json()

# convert the object into a dict
array_of_replication_config_spec_dict = array_of_replication_config_spec_instance.to_dict()
# create an instance of ArrayOfReplicationConfigSpec from a dict
array_of_replication_config_spec_form_dict = array_of_replication_config_spec.from_dict(array_of_replication_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


