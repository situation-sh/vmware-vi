# RemoveDatastoreRequestType

The parameters of *HostDatastoreSystem.RemoveDatastore*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.remove_datastore_request_type import RemoveDatastoreRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveDatastoreRequestType from a JSON string
remove_datastore_request_type_instance = RemoveDatastoreRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveDatastoreRequestType.to_json()

# convert the object into a dict
remove_datastore_request_type_dict = remove_datastore_request_type_instance.to_dict()
# create an instance of RemoveDatastoreRequestType from a dict
remove_datastore_request_type_form_dict = remove_datastore_request_type.from_dict(remove_datastore_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


