# ReplicationFault

Base type for Replication-related errors.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.replication_fault import ReplicationFault

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationFault from a JSON string
replication_fault_instance = ReplicationFault.from_json(json)
# print the JSON string representation of the object
print ReplicationFault.to_json()

# convert the object into a dict
replication_fault_dict = replication_fault_instance.to_dict()
# create an instance of ReplicationFault from a dict
replication_fault_form_dict = replication_fault.from_dict(replication_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


