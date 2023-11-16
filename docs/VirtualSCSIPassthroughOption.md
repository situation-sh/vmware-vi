# VirtualSCSIPassthroughOption

The VirtualSCSIPassthroughOption data object type describes the options for the *VirtualSCSIPassthrough* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_scsi_passthrough_option import VirtualSCSIPassthroughOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSCSIPassthroughOption from a JSON string
virtual_scsi_passthrough_option_instance = VirtualSCSIPassthroughOption.from_json(json)
# print the JSON string representation of the object
print VirtualSCSIPassthroughOption.to_json()

# convert the object into a dict
virtual_scsi_passthrough_option_dict = virtual_scsi_passthrough_option_instance.to_dict()
# create an instance of VirtualSCSIPassthroughOption from a dict
virtual_scsi_passthrough_option_form_dict = virtual_scsi_passthrough_option.from_dict(virtual_scsi_passthrough_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


