# CannotMoveVmWithDeltaDisk

This fault is thrown when an attempt is made to relocate a virtual machine with virtual disk(s) having delta disk backing.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The label of the delta disk device  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.cannot_move_vm_with_delta_disk import CannotMoveVmWithDeltaDisk

# TODO update the JSON string below
json = "{}"
# create an instance of CannotMoveVmWithDeltaDisk from a JSON string
cannot_move_vm_with_delta_disk_instance = CannotMoveVmWithDeltaDisk.from_json(json)
# print the JSON string representation of the object
print CannotMoveVmWithDeltaDisk.to_json()

# convert the object into a dict
cannot_move_vm_with_delta_disk_dict = cannot_move_vm_with_delta_disk_instance.to_dict()
# create an instance of CannotMoveVmWithDeltaDisk from a dict
cannot_move_vm_with_delta_disk_form_dict = cannot_move_vm_with_delta_disk.from_dict(cannot_move_vm_with_delta_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


