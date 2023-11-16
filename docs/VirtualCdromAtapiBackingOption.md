# VirtualCdromAtapiBackingOption

The VirtualCdromOption.AtapiBackingOption data object type contains the options for the ATAPI CD-ROM device backing. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_cdrom_atapi_backing_option import VirtualCdromAtapiBackingOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromAtapiBackingOption from a JSON string
virtual_cdrom_atapi_backing_option_instance = VirtualCdromAtapiBackingOption.from_json(json)
# print the JSON string representation of the object
print VirtualCdromAtapiBackingOption.to_json()

# convert the object into a dict
virtual_cdrom_atapi_backing_option_dict = virtual_cdrom_atapi_backing_option_instance.to_dict()
# create an instance of VirtualCdromAtapiBackingOption from a dict
virtual_cdrom_atapi_backing_option_form_dict = virtual_cdrom_atapi_backing_option.from_dict(virtual_cdrom_atapi_backing_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


