# InsufficientStorageSpace

The fault occurs when Storage DRS cannot perform a given operation (e.g., fix the out of space condition, or place a virtual disk) because there is insufficient storage space in the given storage pod to meet the requirements of the operation.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.insufficient_storage_space import InsufficientStorageSpace

# TODO update the JSON string below
json = "{}"
# create an instance of InsufficientStorageSpace from a JSON string
insufficient_storage_space_instance = InsufficientStorageSpace.from_json(json)
# print the JSON string representation of the object
print InsufficientStorageSpace.to_json()

# convert the object into a dict
insufficient_storage_space_dict = insufficient_storage_space_instance.to_dict()
# create an instance of InsufficientStorageSpace from a dict
insufficient_storage_space_form_dict = insufficient_storage_space.from_dict(insufficient_storage_space_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


