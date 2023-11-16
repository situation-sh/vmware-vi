# ArrayOfVStorageObjectStateInfo

A boxed array of *VStorageObjectStateInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VStorageObjectStateInfo]**](VStorageObjectStateInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_v_storage_object_state_info import ArrayOfVStorageObjectStateInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVStorageObjectStateInfo from a JSON string
array_of_v_storage_object_state_info_instance = ArrayOfVStorageObjectStateInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVStorageObjectStateInfo.to_json()

# convert the object into a dict
array_of_v_storage_object_state_info_dict = array_of_v_storage_object_state_info_instance.to_dict()
# create an instance of ArrayOfVStorageObjectStateInfo from a dict
array_of_v_storage_object_state_info_form_dict = array_of_v_storage_object_state_info.from_dict(array_of_v_storage_object_state_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


