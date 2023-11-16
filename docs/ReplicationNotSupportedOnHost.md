# ReplicationNotSupportedOnHost

Thrown if the replication module is not loaded in the host.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.replication_not_supported_on_host import ReplicationNotSupportedOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationNotSupportedOnHost from a JSON string
replication_not_supported_on_host_instance = ReplicationNotSupportedOnHost.from_json(json)
# print the JSON string representation of the object
print ReplicationNotSupportedOnHost.to_json()

# convert the object into a dict
replication_not_supported_on_host_dict = replication_not_supported_on_host_instance.to_dict()
# create an instance of ReplicationNotSupportedOnHost from a dict
replication_not_supported_on_host_form_dict = replication_not_supported_on_host.from_dict(replication_not_supported_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


