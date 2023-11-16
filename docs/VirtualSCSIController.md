# VirtualSCSIController

The VirtualSCSIController data object type represents a SCSI controller in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hot_add_remove** | **bool** | All SCSI controllers support hot adding and removing of devices.  This support can&#39;t be toggled in the current implementation. Therefore, this option is ignored when reconfiguring a SCSI controller and is always set to \&quot;true\&quot; when reading an existing configuration.  | [optional] 
**shared_bus** | [**VirtualSCSISharingEnum**](VirtualSCSISharingEnum.md) |  | 
**scsi_ctlr_unit_number** | **int** | The unit number of the SCSI controller.  The SCSI controller sits on its own bus, so this field defines which slot the controller is using.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_scsi_controller import VirtualSCSIController

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSCSIController from a JSON string
virtual_scsi_controller_instance = VirtualSCSIController.from_json(json)
# print the JSON string representation of the object
print VirtualSCSIController.to_json()

# convert the object into a dict
virtual_scsi_controller_dict = virtual_scsi_controller_instance.to_dict()
# create an instance of VirtualSCSIController from a dict
virtual_scsi_controller_form_dict = virtual_scsi_controller.from_dict(virtual_scsi_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


