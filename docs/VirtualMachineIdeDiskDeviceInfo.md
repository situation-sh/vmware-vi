# VirtualMachineIdeDiskDeviceInfo

The IdeDiskDeviceInfo class contains detailed information about a specific IDE disk hardware device.  These devices are for the vim.vm.device.VirtualDisk.RawDiskVer2BackingInfo and vim.vm.device.VirtualDisk.PartitionedRawDiskVer2BackingInfo backings. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partition_table** | [**List[VirtualMachineIdeDiskDevicePartitionInfo]**](VirtualMachineIdeDiskDevicePartitionInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_ide_disk_device_info import VirtualMachineIdeDiskDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineIdeDiskDeviceInfo from a JSON string
virtual_machine_ide_disk_device_info_instance = VirtualMachineIdeDiskDeviceInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineIdeDiskDeviceInfo.to_json()

# convert the object into a dict
virtual_machine_ide_disk_device_info_dict = virtual_machine_ide_disk_device_info_instance.to_dict()
# create an instance of VirtualMachineIdeDiskDeviceInfo from a dict
virtual_machine_ide_disk_device_info_form_dict = virtual_machine_ide_disk_device_info.from_dict(virtual_machine_ide_disk_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


