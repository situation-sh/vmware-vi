# VirtualCdromOption

The VirtualCdromOption data object type contains the options for the virtual CD-ROM class. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_cdrom_option import VirtualCdromOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdromOption from a JSON string
virtual_cdrom_option_instance = VirtualCdromOption.from_json(json)
# print the JSON string representation of the object
print VirtualCdromOption.to_json()

# convert the object into a dict
virtual_cdrom_option_dict = virtual_cdrom_option_instance.to_dict()
# create an instance of VirtualCdromOption from a dict
virtual_cdrom_option_form_dict = virtual_cdrom_option.from_dict(virtual_cdrom_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


