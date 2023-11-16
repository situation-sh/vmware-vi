# HostRenameVStorageObjectRequestType

The parameters of *HostVStorageObjectManager.HostRenameVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**name** | **str** | The new name for the virtual storage object.  | 

## Example

```python
from vmware_vi.models.host_rename_v_storage_object_request_type import HostRenameVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostRenameVStorageObjectRequestType from a JSON string
host_rename_v_storage_object_request_type_instance = HostRenameVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print HostRenameVStorageObjectRequestType.to_json()

# convert the object into a dict
host_rename_v_storage_object_request_type_dict = host_rename_v_storage_object_request_type_instance.to_dict()
# create an instance of HostRenameVStorageObjectRequestType from a dict
host_rename_v_storage_object_request_type_form_dict = host_rename_v_storage_object_request_type.from_dict(host_rename_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


