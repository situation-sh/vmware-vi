# BaseConfigInfoRawDiskMappingBackingInfo

This data object type contains information about raw device mapping.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_uuid** | **str** | Unique identifier of the LUN accessed by the raw disk mapping.  ***Since:*** vSphere API 6.5  | 
**compatibility_mode** | **str** | The compatibility mode of the raw disk mapping (RDM).  This must be specified when a new virtual disk with an RDM backing is created.  See also *VirtualDiskCompatibilityMode_enum*.  ***Since:*** vSphere API 6.5  | 

## Example

```python
from vmware_vi.models.base_config_info_raw_disk_mapping_backing_info import BaseConfigInfoRawDiskMappingBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BaseConfigInfoRawDiskMappingBackingInfo from a JSON string
base_config_info_raw_disk_mapping_backing_info_instance = BaseConfigInfoRawDiskMappingBackingInfo.from_json(json)
# print the JSON string representation of the object
print BaseConfigInfoRawDiskMappingBackingInfo.to_json()

# convert the object into a dict
base_config_info_raw_disk_mapping_backing_info_dict = base_config_info_raw_disk_mapping_backing_info_instance.to_dict()
# create an instance of BaseConfigInfoRawDiskMappingBackingInfo from a dict
base_config_info_raw_disk_mapping_backing_info_form_dict = base_config_info_raw_disk_mapping_backing_info.from_dict(base_config_info_raw_disk_mapping_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


