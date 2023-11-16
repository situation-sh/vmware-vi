# HostDeleteVStorageObjectExRequestType

The parameters of *HostVStorageObjectManager.HostDeleteVStorageObjectEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_delete_v_storage_object_ex_request_type import HostDeleteVStorageObjectExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostDeleteVStorageObjectExRequestType from a JSON string
host_delete_v_storage_object_ex_request_type_instance = HostDeleteVStorageObjectExRequestType.from_json(json)
# print the JSON string representation of the object
print HostDeleteVStorageObjectExRequestType.to_json()

# convert the object into a dict
host_delete_v_storage_object_ex_request_type_dict = host_delete_v_storage_object_ex_request_type_instance.to_dict()
# create an instance of HostDeleteVStorageObjectExRequestType from a dict
host_delete_v_storage_object_ex_request_type_form_dict = host_delete_v_storage_object_ex_request_type.from_dict(host_delete_v_storage_object_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


