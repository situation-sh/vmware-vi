# AttachTagToVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.AttachTagToVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**category** | **str** | The category to which the tag belongs.  | 
**tag** | **str** | The tag which has to be associated with the virtual storage object.  | 

## Example

```python
from vmware_vi.models.attach_tag_to_v_storage_object_request_type import AttachTagToVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of AttachTagToVStorageObjectRequestType from a JSON string
attach_tag_to_v_storage_object_request_type_instance = AttachTagToVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print AttachTagToVStorageObjectRequestType.to_json()

# convert the object into a dict
attach_tag_to_v_storage_object_request_type_dict = attach_tag_to_v_storage_object_request_type_instance.to_dict()
# create an instance of AttachTagToVStorageObjectRequestType from a dict
attach_tag_to_v_storage_object_request_type_form_dict = attach_tag_to_v_storage_object_request_type.from_dict(attach_tag_to_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


