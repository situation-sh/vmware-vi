# VirtualDiskRawDiskMappingVer1BackingOption

The VirtualDiskOption.RawDiskMappingVer1BackingOption object type contains the available options when backing a virtual disk using a raw device mapping on ESX Server 2.5 or 3.x. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptor_file_name_extensions** | [**ChoiceOption**](ChoiceOption.md) |  | [optional] 
**compatibility_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**disk_mode** | [**ChoiceOption**](ChoiceOption.md) |  | 
**uuid** | **bool** | Flag to indicate whether this backing supports disk UUID property.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.virtual_disk_raw_disk_mapping_ver1_backing_option import VirtualDiskRawDiskMappingVer1BackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualDiskRawDiskMappingVer1BackingOption from a JSON string
virtual_disk_raw_disk_mapping_ver1_backing_option_instance = VirtualDiskRawDiskMappingVer1BackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualDiskRawDiskMappingVer1BackingOption.to_json()

# convert the object into a dict
virtual_disk_raw_disk_mapping_ver1_backing_option_dict = virtual_disk_raw_disk_mapping_ver1_backing_option_instance.to_dict()
# create an instance of VirtualDiskRawDiskMappingVer1BackingOption from a dict
virtual_disk_raw_disk_mapping_ver1_backing_option_form_dict = virtual_disk_raw_disk_mapping_ver1_backing_option.from_dict(virtual_disk_raw_disk_mapping_ver1_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


