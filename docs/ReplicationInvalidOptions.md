# ReplicationInvalidOptions

A ReplicationInvalidOptions fault is thrown when the options string passed contains invalid characters or broken format.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**options** | **str** | The invalid options string.  ***Since:*** vSphere API 5.0  | 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.replication_invalid_options import ReplicationInvalidOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationInvalidOptions from a JSON string
replication_invalid_options_instance = ReplicationInvalidOptions.from_json(json)
# print the JSON string representation of the object
print ReplicationInvalidOptions.to_json()

# convert the object into a dict
replication_invalid_options_dict = replication_invalid_options_instance.to_dict()
# create an instance of ReplicationInvalidOptions from a dict
replication_invalid_options_form_dict = replication_invalid_options.from_dict(replication_invalid_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


