# VirtualMachineDiskDeviceInfo

The DiskDeviceInfo class contains basic information about a specific disk hardware device. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity** | **int** | Size of disk  | [optional] 
**vm** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | List of known virtual machines using this physical disk as a backing  Refers instances of *VirtualMachine*.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_disk_device_info import VirtualMachineDiskDeviceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineDiskDeviceInfo from a JSON string
virtual_machine_disk_device_info_instance = VirtualMachineDiskDeviceInfo.from_json(json)
# print the JSON string representation of the object
print VirtualMachineDiskDeviceInfo.to_json()

# convert the object into a dict
virtual_machine_disk_device_info_dict = virtual_machine_disk_device_info_instance.to_dict()
# create an instance of VirtualMachineDiskDeviceInfo from a dict
virtual_machine_disk_device_info_form_dict = virtual_machine_disk_device_info.from_dict(virtual_machine_disk_device_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


