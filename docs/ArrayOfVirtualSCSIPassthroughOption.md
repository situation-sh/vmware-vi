# ArrayOfVirtualSCSIPassthroughOption

A boxed array of *VirtualSCSIPassthroughOption*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualSCSIPassthroughOption]**](VirtualSCSIPassthroughOption.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_scsi_passthrough_option import ArrayOfVirtualSCSIPassthroughOption

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualSCSIPassthroughOption from a JSON string
array_of_virtual_scsi_passthrough_option_instance = ArrayOfVirtualSCSIPassthroughOption.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualSCSIPassthroughOption.to_json()

# convert the object into a dict
array_of_virtual_scsi_passthrough_option_dict = array_of_virtual_scsi_passthrough_option_instance.to_dict()
# create an instance of ArrayOfVirtualSCSIPassthroughOption from a dict
array_of_virtual_scsi_passthrough_option_form_dict = array_of_virtual_scsi_passthrough_option.from_dict(array_of_virtual_scsi_passthrough_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


