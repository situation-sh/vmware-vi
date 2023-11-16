# HostRetrieveVStorageObjectMetadataValueRequestType

The parameters of *HostVStorageObjectManager.HostRetrieveVStorageObjectMetadataValue*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**snapshot_id** | [**ID**](ID.md) |  | [optional] 
**key** | **str** | The key for the the virtual storage object  | 

## Example

```python
from vmware_vi.models.host_retrieve_v_storage_object_metadata_value_request_type import HostRetrieveVStorageObjectMetadataValueRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostRetrieveVStorageObjectMetadataValueRequestType from a JSON string
host_retrieve_v_storage_object_metadata_value_request_type_instance = HostRetrieveVStorageObjectMetadataValueRequestType.from_json(json)
# print the JSON string representation of the object
print HostRetrieveVStorageObjectMetadataValueRequestType.to_json()

# convert the object into a dict
host_retrieve_v_storage_object_metadata_value_request_type_dict = host_retrieve_v_storage_object_metadata_value_request_type_instance.to_dict()
# create an instance of HostRetrieveVStorageObjectMetadataValueRequestType from a dict
host_retrieve_v_storage_object_metadata_value_request_type_form_dict = host_retrieve_v_storage_object_metadata_value_request_type.from_dict(host_retrieve_v_storage_object_metadata_value_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


