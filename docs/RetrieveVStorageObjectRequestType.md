# RetrieveVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.RetrieveVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**disk_info_flags** | **List[str]** | Flags indicating the FCD information to be retrieved. If diskInfoFlags is unset, then all FCD information will be retrieved. See *vslmDiskInfoFlag_enum* for the list of supported values.  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_v_storage_object_request_type import RetrieveVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveVStorageObjectRequestType from a JSON string
retrieve_v_storage_object_request_type_instance = RetrieveVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveVStorageObjectRequestType.to_json()

# convert the object into a dict
retrieve_v_storage_object_request_type_dict = retrieve_v_storage_object_request_type_instance.to_dict()
# create an instance of RetrieveVStorageObjectRequestType from a dict
retrieve_v_storage_object_request_type_form_dict = retrieve_v_storage_object_request_type.from_dict(retrieve_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


