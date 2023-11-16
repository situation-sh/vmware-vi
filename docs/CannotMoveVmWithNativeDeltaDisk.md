# CannotMoveVmWithNativeDeltaDisk

This fault is thrown when an attempt is made to migrate a virtual machine with native delta disks to different datastores.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_move_vm_with_native_delta_disk import CannotMoveVmWithNativeDeltaDisk

# TODO update the JSON string below
json = "{}"
# create an instance of CannotMoveVmWithNativeDeltaDisk from a JSON string
cannot_move_vm_with_native_delta_disk_instance = CannotMoveVmWithNativeDeltaDisk.from_json(json)
# print the JSON string representation of the object
print CannotMoveVmWithNativeDeltaDisk.to_json()

# convert the object into a dict
cannot_move_vm_with_native_delta_disk_dict = cannot_move_vm_with_native_delta_disk_instance.to_dict()
# create an instance of CannotMoveVmWithNativeDeltaDisk from a dict
cannot_move_vm_with_native_delta_disk_form_dict = cannot_move_vm_with_native_delta_disk.from_dict(cannot_move_vm_with_native_delta_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


