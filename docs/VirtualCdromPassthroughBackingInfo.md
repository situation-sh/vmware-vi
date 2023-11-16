# VirtualCdromPassthroughBackingInfo

The VirtualCdrom.PassthroughBackingInfo data class represents a device pass-through backing for a virtual CD-ROM. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusive** | **bool** | Flag to indicate whether or not the virtual machine has exclusive CD-ROM device access.  | 

## Example

```python
from vmware_vi.models.virtual_cdrom_passthrough_backing_info import VirtualCdromPassthroughBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromPassthroughBackingInfo from a JSON string
virtual_cdrom_passthrough_backing_info_instance = VirtualCdromPassthroughBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualCdromPassthroughBackingInfo.to_json()

# convert the object into a dict
virtual_cdrom_passthrough_backing_info_dict = virtual_cdrom_passthrough_backing_info_instance.to_dict()
# create an instance of VirtualCdromPassthroughBackingInfo from a dict
virtual_cdrom_passthrough_backing_info_form_dict = virtual_cdrom_passthrough_backing_info.from_dict(virtual_cdrom_passthrough_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


