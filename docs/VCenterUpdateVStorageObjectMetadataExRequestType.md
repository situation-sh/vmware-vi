# VCenterUpdateVStorageObjectMetadataExRequestType

The parameters of *VcenterVStorageObjectManager.VCenterUpdateVStorageObjectMetadataEx_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**metadata** | [**List[KeyValue]**](KeyValue.md) | array of key/value strings. (keys must be unique within the list)  ***Since:*** VI API 2.5  | [optional] 
**delete_keys** | **List[str]** | array of keys need to be deleted  | [optional] 

## Example

```python
from vmware_vi.models.v_center_update_v_storage_object_metadata_ex_request_type import VCenterUpdateVStorageObjectMetadataExRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of VCenterUpdateVStorageObjectMetadataExRequestType from a JSON string
v_center_update_v_storage_object_metadata_ex_request_type_instance = VCenterUpdateVStorageObjectMetadataExRequestType.from_json(json)
# print the JSON string representation of the object
print VCenterUpdateVStorageObjectMetadataExRequestType.to_json()

# convert the object into a dict
v_center_update_v_storage_object_metadata_ex_request_type_dict = v_center_update_v_storage_object_metadata_ex_request_type_instance.to_dict()
# create an instance of VCenterUpdateVStorageObjectMetadataExRequestType from a dict
v_center_update_v_storage_object_metadata_ex_request_type_form_dict = v_center_update_v_storage_object_metadata_ex_request_type.from_dict(v_center_update_v_storage_object_metadata_ex_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


