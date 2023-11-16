# HostDatastoreSystemDatastoreResult

Contains result of remove datastore request.  Used as return value by *HostDatastoreSystem.RemoveDatastoreEx_Task*  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**fault** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_datastore_system_datastore_result import HostDatastoreSystemDatastoreResult

# TODO update the JSON string below
json = "{}"
# create an instance of HostDatastoreSystemDatastoreResult from a JSON string
host_datastore_system_datastore_result_instance = HostDatastoreSystemDatastoreResult.from_json(json)
# print the JSON string representation of the object
print HostDatastoreSystemDatastoreResult.to_json()

# convert the object into a dict
host_datastore_system_datastore_result_dict = host_datastore_system_datastore_result_instance.to_dict()
# create an instance of HostDatastoreSystemDatastoreResult from a dict
host_datastore_system_datastore_result_form_dict = host_datastore_system_datastore_result.from_dict(host_datastore_system_datastore_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


