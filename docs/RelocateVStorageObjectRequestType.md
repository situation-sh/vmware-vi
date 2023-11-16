# RelocateVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.RelocateVStorageObject_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VslmRelocateSpec**](VslmRelocateSpec.md) |  | 

## Example

```python
from vmware_vi.models.relocate_v_storage_object_request_type import RelocateVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RelocateVStorageObjectRequestType from a JSON string
relocate_v_storage_object_request_type_instance = RelocateVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print RelocateVStorageObjectRequestType.to_json()

# convert the object into a dict
relocate_v_storage_object_request_type_dict = relocate_v_storage_object_request_type_instance.to_dict()
# create an instance of RelocateVStorageObjectRequestType from a dict
relocate_v_storage_object_request_type_form_dict = relocate_v_storage_object_request_type.from_dict(relocate_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


