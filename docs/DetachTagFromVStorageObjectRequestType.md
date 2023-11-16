# DetachTagFromVStorageObjectRequestType

The parameters of *VcenterVStorageObjectManager.DetachTagFromVStorageObject*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ID**](ID.md) |  | 
**category** | **str** | The category to which the tag belongs.  | 
**tag** | **str** | The tag which has to be disassociated with the virtual storage object.  | 

## Example

```python
from vmware_vi.models.detach_tag_from_v_storage_object_request_type import DetachTagFromVStorageObjectRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DetachTagFromVStorageObjectRequestType from a JSON string
detach_tag_from_v_storage_object_request_type_instance = DetachTagFromVStorageObjectRequestType.from_json(json)
# print the JSON string representation of the object
print DetachTagFromVStorageObjectRequestType.to_json()

# convert the object into a dict
detach_tag_from_v_storage_object_request_type_dict = detach_tag_from_v_storage_object_request_type_instance.to_dict()
# create an instance of DetachTagFromVStorageObjectRequestType from a dict
detach_tag_from_v_storage_object_request_type_form_dict = detach_tag_from_v_storage_object_request_type.from_dict(detach_tag_from_v_storage_object_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


