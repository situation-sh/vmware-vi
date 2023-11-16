# InvalidDatastore

An InvalidDatastore exception is thrown if an operation fails because of a problem with the specified datastore.  Typically, a subclass of this exception is thrown, indicating a problem such as an inaccessible datastore or an invalid datastore path. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**name** | **str** | The name of the datastore that is invalid.  | [optional] 

## Example

```python
from vmware_vi.models.invalid_datastore import InvalidDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidDatastore from a JSON string
invalid_datastore_instance = InvalidDatastore.from_json(json)
# print the JSON string representation of the object
print InvalidDatastore.to_json()

# convert the object into a dict
invalid_datastore_dict = invalid_datastore_instance.to_dict()
# create an instance of InvalidDatastore from a dict
invalid_datastore_form_dict = invalid_datastore.from_dict(invalid_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


