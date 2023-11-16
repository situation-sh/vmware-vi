# ConcurrentAccess

A ConcurrentAccess fault is thrown when an operation fails because another operation has modified the datastructure.  For non-transactional operations, such as a recursive delete of a subtree of the inventory, the operation might fail with ConcurrentAccess if another thread has added a new entity to the hierarchy. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.concurrent_access import ConcurrentAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ConcurrentAccess from a JSON string
concurrent_access_instance = ConcurrentAccess.from_json(json)
# print the JSON string representation of the object
print ConcurrentAccess.to_json()

# convert the object into a dict
concurrent_access_dict = concurrent_access_instance.to_dict()
# create an instance of ConcurrentAccess from a dict
concurrent_access_form_dict = concurrent_access.from_dict(concurrent_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


