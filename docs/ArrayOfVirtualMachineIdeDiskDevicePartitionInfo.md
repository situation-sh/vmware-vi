# ArrayOfVirtualMachineIdeDiskDevicePartitionInfo

A boxed array of *VirtualMachineIdeDiskDevicePartitionInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineIdeDiskDevicePartitionInfo]**](VirtualMachineIdeDiskDevicePartitionInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_ide_disk_device_partition_info import ArrayOfVirtualMachineIdeDiskDevicePartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineIdeDiskDevicePartitionInfo from a JSON string
array_of_virtual_machine_ide_disk_device_partition_info_instance = ArrayOfVirtualMachineIdeDiskDevicePartitionInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineIdeDiskDevicePartitionInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_ide_disk_device_partition_info_dict = array_of_virtual_machine_ide_disk_device_partition_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineIdeDiskDevicePartitionInfo from a dict
array_of_virtual_machine_ide_disk_device_partition_info_form_dict = array_of_virtual_machine_ide_disk_device_partition_info.from_dict(array_of_virtual_machine_ide_disk_device_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


