# SnapshotIncompatibleDeviceInVm

Thrown if a snapshot operation cannot be performed on account of an incompatible device.  This fault can be thrown for instance if a virtual machine uses a raw disk or a shared bus controller. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.snapshot_incompatible_device_in_vm import SnapshotIncompatibleDeviceInVm

# TODO update the JSON string below
json = "{}"
# create an instance of SnapshotIncompatibleDeviceInVm from a JSON string
snapshot_incompatible_device_in_vm_instance = SnapshotIncompatibleDeviceInVm.from_json(json)
# print the JSON string representation of the object
print SnapshotIncompatibleDeviceInVm.to_json()

# convert the object into a dict
snapshot_incompatible_device_in_vm_dict = snapshot_incompatible_device_in_vm_instance.to_dict()
# create an instance of SnapshotIncompatibleDeviceInVm from a dict
snapshot_incompatible_device_in_vm_form_dict = snapshot_incompatible_device_in_vm.from_dict(snapshot_incompatible_device_in_vm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


