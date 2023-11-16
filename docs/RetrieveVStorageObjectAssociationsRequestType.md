# RetrieveVStorageObjectAssociationsRequestType

The parameters of *VcenterVStorageObjectManager.RetrieveVStorageObjectAssociations*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[RetrieveVStorageObjSpec]**](RetrieveVStorageObjSpec.md) | The IDs of the virtual storage objects of the query.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.retrieve_v_storage_object_associations_request_type import RetrieveVStorageObjectAssociationsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RetrieveVStorageObjectAssociationsRequestType from a JSON string
retrieve_v_storage_object_associations_request_type_instance = RetrieveVStorageObjectAssociationsRequestType.from_json(json)
# print the JSON string representation of the object
print RetrieveVStorageObjectAssociationsRequestType.to_json()

# convert the object into a dict
retrieve_v_storage_object_associations_request_type_dict = retrieve_v_storage_object_associations_request_type_instance.to_dict()
# create an instance of RetrieveVStorageObjectAssociationsRequestType from a dict
retrieve_v_storage_object_associations_request_type_form_dict = retrieve_v_storage_object_associations_request_type.from_dict(retrieve_v_storage_object_associations_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


