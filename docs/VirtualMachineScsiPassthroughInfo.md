# VirtualMachineScsiPassthroughInfo

Description of a generic SCSI device, including information about the device ID. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scsi_class** | **str** | The class of the generic SCSI device.  | 
**vendor** | **str** | The vendor name.  | 
**physical_unit_number** | **int** | Unit number of the generic device on the physical host.  | 

## Example

```python
from vmware_vi.models.virtual_machine_scsi_passthrough_info import VirtualMachineScsiPassthroughInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineScsiPassthroughInfo from a JSON string
virtual_machine_scsi_passthrough_info_instance = VirtualMachineScsiPassthroughInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineScsiPassthroughInfo.to_json()

# convert the object into a dict
virtual_machine_scsi_passthrough_info_dict = virtual_machine_scsi_passthrough_info_instance.to_dict()
# create an instance of VirtualMachineScsiPassthroughInfo from a dict
virtual_machine_scsi_passthrough_info_form_dict = virtual_machine_scsi_passthrough_info.from_dict(virtual_machine_scsi_passthrough_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


