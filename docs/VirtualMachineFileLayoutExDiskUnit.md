# VirtualMachineFileLayoutExDiskUnit

Information about a single unit of a virtual disk, such as the base-disk or a delta-disk.  A disk-unit consists of at least one descriptor file, and zero or more extent files.  Sometimes, a disk-unit is also referred to as a _backing_.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_key** | **List[int]** | Array of keys of the files that make up the disk unit.  Values here correspond to property *VirtualMachineFileLayoutExFileInfo.key* in *VirtualMachineFileLayoutEx.file*.  At least one entry always exists in this array. Property *VirtualMachineFileLayoutExFileInfo.type* of the referenced file can be used to distinguish the disk descriptor (type *diskDescriptor*) from the extents.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_ex_disk_unit import VirtualMachineFileLayoutExDiskUnit

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutExDiskUnit from a JSON string
virtual_machine_file_layout_ex_disk_unit_instance = VirtualMachineFileLayoutExDiskUnit.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutExDiskUnit.to_json()

# convert the object into a dict
virtual_machine_file_layout_ex_disk_unit_dict = virtual_machine_file_layout_ex_disk_unit_instance.to_dict()
# create an instance of VirtualMachineFileLayoutExDiskUnit from a dict
virtual_machine_file_layout_ex_disk_unit_form_dict = virtual_machine_file_layout_ex_disk_unit.from_dict(virtual_machine_file_layout_ex_disk_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


