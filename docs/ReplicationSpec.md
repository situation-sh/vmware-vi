# ReplicationSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_group_id** | [**ReplicationGroupId**](ReplicationGroupId.md) |  | 

## Example

```python
from vmware_vi.models.replication_spec import ReplicationSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationSpec from a JSON string
replication_spec_instance = ReplicationSpec.from_json(json)
# print the JSON string representation of the object
print ReplicationSpec.to_json()

# convert the object into a dict
replication_spec_dict = replication_spec_instance.to_dict()
# create an instance of ReplicationSpec from a dict
replication_spec_form_dict = replication_spec.from_dict(replication_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


