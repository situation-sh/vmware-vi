# VirtualMachineFileLayoutExDiskLayout

Layout of a virtual disk, including the base- and delta- disks.  A virtual disk typically is made up of a chain of disk-units.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | Identifier for the virtual disk in *VirtualHardware.device*.  ***Since:*** vSphere API 4.0  | 
**chain** | [**List[VirtualMachineFileLayoutExDiskUnit]**](VirtualMachineFileLayoutExDiskUnit.md) | The disk-unit chain that makes up this virtual disk.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_ex_disk_layout import VirtualMachineFileLayoutExDiskLayout

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutExDiskLayout from a JSON string
virtual_machine_file_layout_ex_disk_layout_instance = VirtualMachineFileLayoutExDiskLayout.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutExDiskLayout.to_json()

# convert the object into a dict
virtual_machine_file_layout_ex_disk_layout_dict = virtual_machine_file_layout_ex_disk_layout_instance.to_dict()
# create an instance of VirtualMachineFileLayoutExDiskLayout from a dict
virtual_machine_file_layout_ex_disk_layout_form_dict = virtual_machine_file_layout_ex_disk_layout.from_dict(virtual_machine_file_layout_ex_disk_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


