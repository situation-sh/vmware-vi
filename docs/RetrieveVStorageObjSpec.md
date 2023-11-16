# RetrieveVStorageObjSpec

This data object is a pair of the virtural storage object id and its datastore.  ***Since:*** vSphere API 6.7 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.retrieve_v_storage_obj_spec import RetrieveVStorageObjSpec

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveVStorageObjSpec from a JSON string
retrieve_v_storage_obj_spec_instance = RetrieveVStorageObjSpec.from_json(json)
# print the JSON string representation of the object
print RetrieveVStorageObjSpec.to_json()

# convert the object into a dict
retrieve_v_storage_obj_spec_dict = retrieve_v_storage_obj_spec_instance.to_dict()
# create an instance of RetrieveVStorageObjSpec from a dict
retrieve_v_storage_obj_spec_form_dict = retrieve_v_storage_obj_spec.from_dict(retrieve_v_storage_obj_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


