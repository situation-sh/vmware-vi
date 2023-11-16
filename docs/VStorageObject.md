# VStorageObject

This data object type describes a virtual storage object.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**VStorageObjectConfigInfo**](VStorageObjectConfigInfo.md) |  | 

## Example

```python
from vmware_vi.models.v_storage_object import VStorageObject

# TODO update the JSON string below
json = "{}"
# create an instance of VStorageObject from a JSON string
v_storage_object_instance = VStorageObject.from_json(json)
# print the JSON string representation of the object
print VStorageObject.to_json()

# convert the object into a dict
v_storage_object_dict = v_storage_object_instance.to_dict()
# create an instance of VStorageObject from a dict
v_storage_object_form_dict = v_storage_object.from_dict(v_storage_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


