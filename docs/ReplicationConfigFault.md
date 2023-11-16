# ReplicationConfigFault

Base type for Replication-related configuration errors.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.replication_config_fault import ReplicationConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationConfigFault from a JSON string
replication_config_fault_instance = ReplicationConfigFault.from_json(json)
# print the JSON string representation of the object
print ReplicationConfigFault.to_json()

# convert the object into a dict
replication_config_fault_dict = replication_config_fault_instance.to_dict()
# create an instance of ReplicationConfigFault from a dict
replication_config_fault_form_dict = replication_config_fault.from_dict(replication_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


