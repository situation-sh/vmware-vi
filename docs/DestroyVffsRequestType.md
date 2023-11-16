# DestroyVffsRequestType

The parameters of *HostStorageSystem.DestroyVffs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_path** | **str** | The path of the VFFS to destroy. See *FileSystemMountInfo*.  | 

## Example

```python
from vmware_vi.models.destroy_vffs_request_type import DestroyVffsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DestroyVffsRequestType from a JSON string
destroy_vffs_request_type_instance = DestroyVffsRequestType.from_json(json)
# print the JSON string representation of the object
print DestroyVffsRequestType.to_json()

# convert the object into a dict
destroy_vffs_request_type_dict = destroy_vffs_request_type_instance.to_dict()
# create an instance of DestroyVffsRequestType from a dict
destroy_vffs_request_type_form_dict = destroy_vffs_request_type.from_dict(destroy_vffs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


