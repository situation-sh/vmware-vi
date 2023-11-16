# ExtendVffsRequestType

The parameters of *HostStorageSystem.ExtendVffs*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vffs_path** | **str** | The path of the VFFS to extend. See *FileSystemMountInfo*.  | 
**device_path** | **str** | Device path of the SSD disk.  | 
**spec** | [**HostDiskPartitionSpec**](HostDiskPartitionSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.extend_vffs_request_type import ExtendVffsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendVffsRequestType from a JSON string
extend_vffs_request_type_instance = ExtendVffsRequestType.from_json(json)
# print the JSON string representation of the object
print ExtendVffsRequestType.to_json()

# convert the object into a dict
extend_vffs_request_type_dict = extend_vffs_request_type_instance.to_dict()
# create an instance of ExtendVffsRequestType from a dict
extend_vffs_request_type_form_dict = extend_vffs_request_type.from_dict(extend_vffs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


