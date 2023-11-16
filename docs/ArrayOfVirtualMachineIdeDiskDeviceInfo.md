# ArrayOfVirtualMachineIdeDiskDeviceInfo

A boxed array of *VirtualMachineIdeDiskDeviceInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineIdeDiskDeviceInfo]**](VirtualMachineIdeDiskDeviceInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_ide_disk_device_info import ArrayOfVirtualMachineIdeDiskDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineIdeDiskDeviceInfo from a JSON string
array_of_virtual_machine_ide_disk_device_info_instance = ArrayOfVirtualMachineIdeDiskDeviceInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineIdeDiskDeviceInfo.to_json()

# convert the object into a dict
array_of_virtual_machine_ide_disk_device_info_dict = array_of_virtual_machine_ide_disk_device_info_instance.to_dict()
# create an instance of ArrayOfVirtualMachineIdeDiskDeviceInfo from a dict
array_of_virtual_machine_ide_disk_device_info_form_dict = array_of_virtual_machine_ide_disk_device_info.from_dict(array_of_virtual_machine_ide_disk_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


