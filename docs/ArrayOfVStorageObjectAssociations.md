# ArrayOfVStorageObjectAssociations

A boxed array of *VStorageObjectAssociations*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VStorageObjectAssociations]**](VStorageObjectAssociations.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_storage_object_associations import ArrayOfVStorageObjectAssociations

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVStorageObjectAssociations from a JSON string
array_of_v_storage_object_associations_instance = ArrayOfVStorageObjectAssociations.from_json(json)
# print the JSON string representation of the object
print ArrayOfVStorageObjectAssociations.to_json()

# convert the object into a dict
array_of_v_storage_object_associations_dict = array_of_v_storage_object_associations_instance.to_dict()
# create an instance of ArrayOfVStorageObjectAssociations from a dict
array_of_v_storage_object_associations_form_dict = array_of_v_storage_object_associations.from_dict(array_of_v_storage_object_associations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


