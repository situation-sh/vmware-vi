# VirtualCdromIsoBackingOption

The VirtualCdromOption.IsoBackingOption data object type contains the options for an ISO image backing. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_cdrom_iso_backing_option import VirtualCdromIsoBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromIsoBackingOption from a JSON string
virtual_cdrom_iso_backing_option_instance = VirtualCdromIsoBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualCdromIsoBackingOption.to_json()

# convert the object into a dict
virtual_cdrom_iso_backing_option_dict = virtual_cdrom_iso_backing_option_instance.to_dict()
# create an instance of VirtualCdromIsoBackingOption from a dict
virtual_cdrom_iso_backing_option_form_dict = virtual_cdrom_iso_backing_option.from_dict(virtual_cdrom_iso_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


