# HostRetrieveVStorageObjectRequestType

The parameters of *HostVStorageObjectManager.HostRetrieveVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**disk_info_flags** | **List[str]** | Flags indicating the FCD information to be retrieved. If diskInfoFlags is unset, then all FCD information will be retrieved. See *vslmDiskInfoFlag_enum* for the list of supported values.  | [optional] 

## Example

```python
from vmware_vi.models.host_retrieve_v_storage_object_request_type import HostRetrieveVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of HostRetrieveVStorageObjectRequestType from a JSON string
host_retrieve_v_storage_object_request_type_instance = HostRetrieveVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print HostRetrieveVStorageObjectRequestType.to_json()

# convert the object into a dict
host_retrieve_v_storage_object_request_type_dict = host_retrieve_v_storage_object_request_type_instance.to_dict()
# create an instance of HostRetrieveVStorageObjectRequestType from a dict
host_retrieve_v_storage_object_request_type_form_dict = host_retrieve_v_storage_object_request_type.from_dict(host_retrieve_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


