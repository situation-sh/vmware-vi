# VirtualCdromPassthroughBackingOption

The VirtualCdromOption.PassthroughBackingOption data object type contains the options for a pass-through CD-ROM device backing. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclusive** | [**BoolOption**](BoolOption.md) |  | 

## Example

```python
from vmware_vi.models.virtual_cdrom_passthrough_backing_option import VirtualCdromPassthroughBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromPassthroughBackingOption from a JSON string
virtual_cdrom_passthrough_backing_option_instance = VirtualCdromPassthroughBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualCdromPassthroughBackingOption.to_json()

# convert the object into a dict
virtual_cdrom_passthrough_backing_option_dict = virtual_cdrom_passthrough_backing_option_instance.to_dict()
# create an instance of VirtualCdromPassthroughBackingOption from a dict
virtual_cdrom_passthrough_backing_option_form_dict = virtual_cdrom_passthrough_backing_option.from_dict(virtual_cdrom_passthrough_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


