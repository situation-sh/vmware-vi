# VirtualSCSIPassthrough

The VirtualSCSIPassthrough data object type contains information about a SCSI device on the virtual machine that is being backed by a generic SCSI device on the host via passthrough. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_scsi_passthrough import VirtualSCSIPassthrough

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSCSIPassthrough from a JSON string
virtual_scsi_passthrough_instance = VirtualSCSIPassthrough.from_json(json)
# print the JSON string representation of the object
print VirtualSCSIPassthrough.to_json()

# convert the object into a dict
virtual_scsi_passthrough_dict = virtual_scsi_passthrough_instance.to_dict()
# create an instance of VirtualSCSIPassthrough from a dict
virtual_scsi_passthrough_form_dict = virtual_scsi_passthrough.from_dict(virtual_scsi_passthrough_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


