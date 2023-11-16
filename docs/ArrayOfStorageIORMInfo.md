# ArrayOfStorageIORMInfo

A boxed array of *StorageIORMInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageIORMInfo]**](StorageIORMInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_iorm_info import ArrayOfStorageIORMInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageIORMInfo from a JSON string
array_of_storage_iorm_info_instance = ArrayOfStorageIORMInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageIORMInfo.to_json()

# convert the object into a dict
array_of_storage_iorm_info_dict = array_of_storage_iorm_info_instance.to_dict()
# create an instance of ArrayOfStorageIORMInfo from a dict
array_of_storage_iorm_info_form_dict = array_of_storage_iorm_info.from_dict(array_of_storage_iorm_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


