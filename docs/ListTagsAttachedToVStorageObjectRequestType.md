# ListTagsAttachedToVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.ListTagsAttachedToVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 

## Example

```python
from vmware_vi.models.list_tags_attached_to_v_storage_object_request_type import ListTagsAttachedToVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListTagsAttachedToVStorageObjectRequestType from a JSON string
list_tags_attached_to_v_storage_object_request_type_instance = ListTagsAttachedToVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print ListTagsAttachedToVStorageObjectRequestType.to_json()

# convert the object into a dict
list_tags_attached_to_v_storage_object_request_type_dict = list_tags_attached_to_v_storage_object_request_type_instance.to_dict()
# create an instance of ListTagsAttachedToVStorageObjectRequestType from a dict
list_tags_attached_to_v_storage_object_request_type_form_dict = list_tags_attached_to_v_storage_object_request_type.from_dict(list_tags_attached_to_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


