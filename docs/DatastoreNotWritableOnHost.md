# DatastoreNotWritableOnHost

This exception is thrown if a datastore is not writable on the target host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.datastore_not_writable_on_host import DatastoreNotWritableOnHost

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreNotWritableOnHost from a JSON string
datastore_not_writable_on_host_instance = DatastoreNotWritableOnHost.from_json(json)
# print the JSON string representation of the object
print DatastoreNotWritableOnHost.to_json()

# convert the object into a dict
datastore_not_writable_on_host_dict = datastore_not_writable_on_host_instance.to_dict()
# create an instance of DatastoreNotWritableOnHost from a dict
datastore_not_writable_on_host_form_dict = datastore_not_writable_on_host.from_dict(datastore_not_writable_on_host_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


