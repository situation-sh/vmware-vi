# DeleteVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.DeleteVStorageObject_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.delete_v_storage_object_request_type import DeleteVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVStorageObjectRequestType from a JSON string
delete_v_storage_object_request_type_instance = DeleteVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print DeleteVStorageObjectRequestType.to_json()

# convert the object into a dict
delete_v_storage_object_request_type_dict = delete_v_storage_object_request_type_instance.to_dict()
# create an instance of DeleteVStorageObjectRequestType from a dict
delete_v_storage_object_request_type_form_dict = delete_v_storage_object_request_type.from_dict(delete_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


