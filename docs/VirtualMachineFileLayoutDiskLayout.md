# VirtualMachineFileLayoutDiskLayout

Enumerats the set of files for each virtual disk. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** | Identification of the disk in *config*.  | 
**disk_file** | **List[str]** | List of files that makes up the virtual disk.  At least one entry always exists in this array. The first entry is the main descriptor of the virtual disk (the one used when adding the disk to a virtual machine). These are complete datastore paths, not relative paths.  | 

## Example

```python
from vmware_vi.models.virtual_machine_file_layout_disk_layout import VirtualMachineFileLayoutDiskLayout

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineFileLayoutDiskLayout from a JSON string
virtual_machine_file_layout_disk_layout_instance = VirtualMachineFileLayoutDiskLayout.from_json(json)
# print the JSON string representation of the object
print VirtualMachineFileLayoutDiskLayout.to_json()

# convert the object into a dict
virtual_machine_file_layout_disk_layout_dict = virtual_machine_file_layout_disk_layout_instance.to_dict()
# create an instance of VirtualMachineFileLayoutDiskLayout from a dict
virtual_machine_file_layout_disk_layout_form_dict = virtual_machine_file_layout_disk_layout.from_dict(virtual_machine_file_layout_disk_layout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


