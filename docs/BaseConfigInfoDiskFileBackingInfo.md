# BaseConfigInfoDiskFileBackingInfo

The data object type for disk file backing of a virtual storage object.  Disk file backing provides full virtualization of the backend storage.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioning_type** | **str** | Provisioning type.  See *BaseConfigInfoDiskFileBackingInfoProvisioningType_enum* for the supported types.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.base_config_info_disk_file_backing_info import BaseConfigInfoDiskFileBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConfigInfoDiskFileBackingInfo from a JSON string
base_config_info_disk_file_backing_info_instance = BaseConfigInfoDiskFileBackingInfo.from_json(json)
# print the JSON string representation of the object
print BaseConfigInfoDiskFileBackingInfo.to_json()

# convert the object into a dict
base_config_info_disk_file_backing_info_dict = base_config_info_disk_file_backing_info_instance.to_dict()
# create an instance of BaseConfigInfoDiskFileBackingInfo from a dict
base_config_info_disk_file_backing_info_form_dict = base_config_info_disk_file_backing_info.from_dict(base_config_info_disk_file_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


