# ArrayOfVStorageObject

A boxed array of *VStorageObject*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VStorageObject]**](VStorageObject.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_storage_object import ArrayOfVStorageObject

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVStorageObject from a JSON string
array_of_v_storage_object_instance = ArrayOfVStorageObject.from_json(json)
# print the JSON string representation of the object
print ArrayOfVStorageObject.to_json()

# convert the object into a dict
array_of_v_storage_object_dict = array_of_v_storage_object_instance.to_dict()
# create an instance of ArrayOfVStorageObject from a dict
array_of_v_storage_object_form_dict = array_of_v_storage_object.from_dict(array_of_v_storage_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


