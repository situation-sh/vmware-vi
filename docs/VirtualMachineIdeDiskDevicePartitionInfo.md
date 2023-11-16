# VirtualMachineIdeDiskDevicePartitionInfo

Describes the partition sizes 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identification of the partition  | 
**capacity** | **int** | Size of partition  | 

## Example

```python
from vmware_vi.models.virtual_machine_ide_disk_device_partition_info import VirtualMachineIdeDiskDevicePartitionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineIdeDiskDevicePartitionInfo from a JSON string
virtual_machine_ide_disk_device_partition_info_instance = VirtualMachineIdeDiskDevicePartitionInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineIdeDiskDevicePartitionInfo.to_json()

# convert the object into a dict
virtual_machine_ide_disk_device_partition_info_dict = virtual_machine_ide_disk_device_partition_info_instance.to_dict()
# create an instance of VirtualMachineIdeDiskDevicePartitionInfo from a dict
virtual_machine_ide_disk_device_partition_info_form_dict = virtual_machine_ide_disk_device_partition_info.from_dict(virtual_machine_ide_disk_device_partition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


