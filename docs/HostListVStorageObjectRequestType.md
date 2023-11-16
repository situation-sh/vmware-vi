# HostListVStorageObjectRequestType

The parameters of *HostVStorageObjectManager.HostListVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.host_list_v_storage_object_request_type import HostListVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostListVStorageObjectRequestType from a JSON string
host_list_v_storage_object_request_type_instance = HostListVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print HostListVStorageObjectRequestType.to_json()

# convert the object into a dict
host_list_v_storage_object_request_type_dict = host_list_v_storage_object_request_type_instance.to_dict()
# create an instance of HostListVStorageObjectRequestType from a dict
host_list_v_storage_object_request_type_form_dict = host_list_v_storage_object_request_type.from_dict(host_list_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


