# VirtualSCSIControllerOption

The VirtualSCSIControllerOption data object type contains the options for a virtual SCSI controller defined by the *VirtualSCSIController* data object type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_scsi_disks** | [**IntOption**](IntOption.md) |  | 
**num_scsi_cdroms** | [**IntOption**](IntOption.md) |  | 
**num_scsi_passthrough** | [**IntOption**](IntOption.md) |  | 
**sharing** | [**List[VirtualSCSISharingEnum]**](VirtualSCSISharingEnum.md) | Supported shared bus modes.  | 
**default_shared_index** | **int** | Index into sharing array specifying the default value.  | 
**hot_add_remove** | [**BoolOption**](BoolOption.md) |  | 
**scsi_ctlr_unit_number** | **int** | The unit number of the SCSI controller.  The SCSI controller sits on its own bus, so that this field defines which slot the controller will use.  | 

## Example

```python
from vmware_vi.models.virtual_scsi_controller_option import VirtualSCSIControllerOption

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualSCSIControllerOption from a JSON string
virtual_scsi_controller_option_instance = VirtualSCSIControllerOption.from_json(json)
# print the JSON string representation of the object
print VirtualSCSIControllerOption.to_json()

# convert the object into a dict
virtual_scsi_controller_option_dict = virtual_scsi_controller_option_instance.to_dict()
# create an instance of VirtualSCSIControllerOption from a dict
virtual_scsi_controller_option_form_dict = virtual_scsi_controller_option.from_dict(virtual_scsi_controller_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


