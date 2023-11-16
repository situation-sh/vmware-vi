# CloneVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.CloneVStorageObject_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**spec** | [**VslmCloneSpec**](VslmCloneSpec.md) |  | 

## Example

```python
from vmware_vi.models.clone_v_storage_object_request_type import CloneVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of CloneVStorageObjectRequestType from a JSON string
clone_v_storage_object_request_type_instance = CloneVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print CloneVStorageObjectRequestType.to_json()

# convert the object into a dict
clone_v_storage_object_request_type_dict = clone_v_storage_object_request_type_instance.to_dict()
# create an instance of CloneVStorageObjectRequestType from a dict
clone_v_storage_object_request_type_form_dict = clone_v_storage_object_request_type.from_dict(clone_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


