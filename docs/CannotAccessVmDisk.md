# CannotAccessVmDisk

One of the virtual machine's virtual disks is not accessible. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.cannot_access_vm_disk import CannotAccessVmDisk

# TODO update the JSON string below
json = "{}"
# create an instance of CannotAccessVmDisk from a JSON string
cannot_access_vm_disk_instance = CannotAccessVmDisk.from_json(json)
# print the JSON string representation of the object
print CannotAccessVmDisk.to_json()

# convert the object into a dict
cannot_access_vm_disk_dict = cannot_access_vm_disk_instance.to_dict()
# create an instance of CannotAccessVmDisk from a dict
cannot_access_vm_disk_form_dict = cannot_access_vm_disk.from_dict(cannot_access_vm_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


