# RenameVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.RenameVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | The new name for the virtual storage object.  | 

## Example

```python
from vmware_vi.models.rename_v_storage_object_request_type import RenameVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RenameVStorageObjectRequestType from a JSON string
rename_v_storage_object_request_type_instance = RenameVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print RenameVStorageObjectRequestType.to_json()

# convert the object into a dict
rename_v_storage_object_request_type_dict = rename_v_storage_object_request_type_instance.to_dict()
# create an instance of RenameVStorageObjectRequestType from a dict
rename_v_storage_object_request_type_form_dict = rename_v_storage_object_request_type.from_dict(rename_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


