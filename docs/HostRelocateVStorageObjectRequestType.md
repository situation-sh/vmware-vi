# HostRelocateVStorageObjectRequestType

The parameters of *HostVStorageObjectManager.HostRelocateVStorageObject_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VslmRelocateSpec**](VslmRelocateSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_relocate_v_storage_object_request_type import HostRelocateVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostRelocateVStorageObjectRequestType from a JSON string
host_relocate_v_storage_object_request_type_instance = HostRelocateVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print HostRelocateVStorageObjectRequestType.to_json()

# convert the object into a dict
host_relocate_v_storage_object_request_type_dict = host_relocate_v_storage_object_request_type_instance.to_dict()
# create an instance of HostRelocateVStorageObjectRequestType from a dict
host_relocate_v_storage_object_request_type_form_dict = host_relocate_v_storage_object_request_type.from_dict(host_relocate_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


