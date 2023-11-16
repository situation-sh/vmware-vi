# RetrieveVStorageObjectStateRequestType

The parameters of *VcenterVStorageObjectManager.RetrieveVStorageObjectState*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_v_storage_object_state_request_type import RetrieveVStorageObjectStateRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveVStorageObjectStateRequestType from a JSON string
retrieve_v_storage_object_state_request_type_instance = RetrieveVStorageObjectStateRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveVStorageObjectStateRequestType.to_json()

# convert the object into a dict
retrieve_v_storage_object_state_request_type_dict = retrieve_v_storage_object_state_request_type_instance.to_dict()
# create an instance of RetrieveVStorageObjectStateRequestType from a dict
retrieve_v_storage_object_state_request_type_form_dict = retrieve_v_storage_object_state_request_type.from_dict(retrieve_v_storage_object_state_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


