# RevertVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.RevertVStorageObject_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | 

## Example

```python
from vmware_vi.models.revert_v_storage_object_request_type import RevertVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RevertVStorageObjectRequestType from a JSON string
revert_v_storage_object_request_type_instance = RevertVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print RevertVStorageObjectRequestType.to_json()

# convert the object into a dict
revert_v_storage_object_request_type_dict = revert_v_storage_object_request_type_instance.to_dict()
# create an instance of RevertVStorageObjectRequestType from a dict
revert_v_storage_object_request_type_form_dict = revert_v_storage_object_request_type.from_dict(revert_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


