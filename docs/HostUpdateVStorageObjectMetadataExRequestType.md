# HostUpdateVStorageObjectMetadataExRequestType

The parameters of *HostVStorageObjectManager.HostUpdateVStorageObjectMetadataEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**metadata** | [**List[KeyValue]**](KeyValue.md) | array of key/value strings. (keys must be unique within the list)  ***Since:*** VI API 2.5  | [optional] 
**delete_keys** | **List[str]** | array of keys need to be deleted  | [optional] 

## Example

```python
from vmware_vi.models.host_update_v_storage_object_metadata_ex_request_type import HostUpdateVStorageObjectMetadataExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostUpdateVStorageObjectMetadataExRequestType from a JSON string
host_update_v_storage_object_metadata_ex_request_type_instance = HostUpdateVStorageObjectMetadataExRequestType.from_json(json)
# print the JSON string representation of the object
print HostUpdateVStorageObjectMetadataExRequestType.to_json()

# convert the object into a dict
host_update_v_storage_object_metadata_ex_request_type_dict = host_update_v_storage_object_metadata_ex_request_type_instance.to_dict()
# create an instance of HostUpdateVStorageObjectMetadataExRequestType from a dict
host_update_v_storage_object_metadata_ex_request_type_form_dict = host_update_v_storage_object_metadata_ex_request_type.from_dict(host_update_v_storage_object_metadata_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


