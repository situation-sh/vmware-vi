# ListVStorageObjectsAttachedToTagRequestType

The parameters of *VcenterVStorageObjectManager.ListVStorageObjectsAttachedToTag*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category to which the tag belongs.  | 
**tag** | **str** | The tag to be queried.  | 

## Example

```python
from vmware_vi.models.list_v_storage_objects_attached_to_tag_request_type import ListVStorageObjectsAttachedToTagRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ListVStorageObjectsAttachedToTagRequestType from a JSON string
list_v_storage_objects_attached_to_tag_request_type_instance = ListVStorageObjectsAttachedToTagRequestType.from_json(json)
# print the JSON string representation of the object
print ListVStorageObjectsAttachedToTagRequestType.to_json()

# convert the object into a dict
list_v_storage_objects_attached_to_tag_request_type_dict = list_v_storage_objects_attached_to_tag_request_type_instance.to_dict()
# create an instance of ListVStorageObjectsAttachedToTagRequestType from a dict
list_v_storage_objects_attached_to_tag_request_type_form_dict = list_v_storage_objects_attached_to_tag_request_type.from_dict(list_v_storage_objects_attached_to_tag_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


