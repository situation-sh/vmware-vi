# HostCloneVStorageObjectRequestType

The parameters of *HostVStorageObjectManager.HostCloneVStorageObject_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VslmCloneSpec**](VslmCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_clone_v_storage_object_request_type import HostCloneVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostCloneVStorageObjectRequestType from a JSON string
host_clone_v_storage_object_request_type_instance = HostCloneVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print HostCloneVStorageObjectRequestType.to_json()

# convert the object into a dict
host_clone_v_storage_object_request_type_dict = host_clone_v_storage_object_request_type_instance.to_dict()
# create an instance of HostCloneVStorageObjectRequestType from a dict
host_clone_v_storage_object_request_type_form_dict = host_clone_v_storage_object_request_type.from_dict(host_clone_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


