# ListVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.ListVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.list_v_storage_object_request_type import ListVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListVStorageObjectRequestType from a JSON string
list_v_storage_object_request_type_instance = ListVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print ListVStorageObjectRequestType.to_json()

# convert the object into a dict
list_v_storage_object_request_type_dict = list_v_storage_object_request_type_instance.to_dict()
# create an instance of ListVStorageObjectRequestType from a dict
list_v_storage_object_request_type_form_dict = list_v_storage_object_request_type.from_dict(list_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


