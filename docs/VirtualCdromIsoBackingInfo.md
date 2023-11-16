# VirtualCdromIsoBackingInfo

The VirtualCdrom.IsoBackingInfo data class represents an ISO backing for a virtual CD-ROM. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_cdrom_iso_backing_info import VirtualCdromIsoBackingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromIsoBackingInfo from a JSON string
virtual_cdrom_iso_backing_info_instance = VirtualCdromIsoBackingInfo.from_json(json)
# print the JSON string representation of the object
print VirtualCdromIsoBackingInfo.to_json()

# convert the object into a dict
virtual_cdrom_iso_backing_info_dict = virtual_cdrom_iso_backing_info_instance.to_dict()
# create an instance of VirtualCdromIsoBackingInfo from a dict
virtual_cdrom_iso_backing_info_form_dict = virtual_cdrom_iso_backing_info.from_dict(virtual_cdrom_iso_backing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


