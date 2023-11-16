# ManagedObjectNotFound

A ManagedObjectNotFound exception is thrown when a request refers to a managed object that no longer exists or has never existed. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.managed_object_not_found import ManagedObjectNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedObjectNotFound from a JSON string
managed_object_not_found_instance = ManagedObjectNotFound.from_json(json)
# print the JSON string representation of the object
print ManagedObjectNotFound.to_json()

# convert the object into a dict
managed_object_not_found_dict = managed_object_not_found_instance.to_dict()
# create an instance of ManagedObjectNotFound from a dict
managed_object_not_found_form_dict = managed_object_not_found.from_dict(managed_object_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


