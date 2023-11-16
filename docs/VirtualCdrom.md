# VirtualCdrom

The VirtualCdrom data object type describes the configuration of a CD-ROM device in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_cdrom import VirtualCdrom

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualCdrom from a JSON string
virtual_cdrom_instance = VirtualCdrom.from_json(json)
# print the JSON string representation of the object
print VirtualCdrom.to_json()

# convert the object into a dict
virtual_cdrom_dict = virtual_cdrom_instance.to_dict()
# create an instance of VirtualCdrom from a dict
virtual_cdrom_form_dict = virtual_cdrom.from_dict(virtual_cdrom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


