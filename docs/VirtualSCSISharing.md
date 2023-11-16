# VirtualSCSISharing

A boxed *VirtualSCSISharing_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualSCSISharingEnum**](VirtualSCSISharingEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_scsi_sharing import VirtualSCSISharing

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSCSISharing from a JSON string
virtual_scsi_sharing_instance = VirtualSCSISharing.from_json(json)
# print the JSON string representation of the object
print VirtualSCSISharing.to_json()

# convert the object into a dict
virtual_scsi_sharing_dict = virtual_scsi_sharing_instance.to_dict()
# create an instance of VirtualSCSISharing from a dict
virtual_scsi_sharing_form_dict = virtual_scsi_sharing.from_dict(virtual_scsi_sharing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


