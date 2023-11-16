# VirtualMachineScsiDiskDeviceInfo

The ScsiDiskDeviceInfo class contains detailed information about a specific scsi disk hardware device.  These devices are for the vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | [**HostScsiDisk**](HostScsiDisk.md) |  | [optional] 
**transport_hint** | **str** | Transport identifier hint used to identify the device.  To definitively correlate this device with a host physical disk, use the disk property. This identifier is intended as a hint to end users to identify the disk device.  ***Since:*** vSphere API 4.0  | [optional] 
**lun_number** | **int** | LUN number hint used to identify the SCSI device.  To definitively correlate this device with a host physical disk, use the disk property. This identifier is intended as a hint to end users to identify the disk device.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_scsi_disk_device_info import VirtualMachineScsiDiskDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineScsiDiskDeviceInfo from a JSON string
virtual_machine_scsi_disk_device_info_instance = VirtualMachineScsiDiskDeviceInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineScsiDiskDeviceInfo.to_json()

# convert the object into a dict
virtual_machine_scsi_disk_device_info_dict = virtual_machine_scsi_disk_device_info_instance.to_dict()
# create an instance of VirtualMachineScsiDiskDeviceInfo from a dict
virtual_machine_scsi_disk_device_info_form_dict = virtual_machine_scsi_disk_device_info.from_dict(virtual_machine_scsi_disk_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


