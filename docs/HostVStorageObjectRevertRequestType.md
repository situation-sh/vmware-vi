# HostVStorageObjectRevertRequestType

The parameters of *HostVStorageObjectManager.HostVStorageObjectRevert_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | 

## Example

```python
from vmware_vi.models.host_v_storage_object_revert_request_type import HostVStorageObjectRevertRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostVStorageObjectRevertRequestType from a JSON string
host_v_storage_object_revert_request_type_instance = HostVStorageObjectRevertRequestType.from_json(json)
# print the JSON string representation of the object
print HostVStorageObjectRevertRequestType.to_json()

# convert the object into a dict
host_v_storage_object_revert_request_type_dict = host_v_storage_object_revert_request_type_instance.to_dict()
# create an instance of HostVStorageObjectRevertRequestType from a dict
host_v_storage_object_revert_request_type_form_dict = host_v_storage_object_revert_request_type.from_dict(host_v_storage_object_revert_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


