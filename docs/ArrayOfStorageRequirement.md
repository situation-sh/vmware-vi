# ArrayOfStorageRequirement

A boxed array of *StorageRequirement*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[StorageRequirement]**](StorageRequirement.md) |  | 

## Example

```python
from vmware_vi.models.array_of_storage_requirement import ArrayOfStorageRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfStorageRequirement from a JSON string
array_of_storage_requirement_instance = ArrayOfStorageRequirement.from_json(json)
# print the JSON string representation of the object
print ArrayOfStorageRequirement.to_json()

# convert the object into a dict
array_of_storage_requirement_dict = array_of_storage_requirement_instance.to_dict()
# create an instance of ArrayOfStorageRequirement from a dict
array_of_storage_requirement_form_dict = array_of_storage_requirement.from_dict(array_of_storage_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


