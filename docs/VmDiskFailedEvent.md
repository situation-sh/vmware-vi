# VmDiskFailedEvent

This event records a failure to create a virtual disk in a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | **str** | The name of the virtual disk.  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_disk_failed_event import VmDiskFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDiskFailedEvent from a JSON string
vm_disk_failed_event_instance = VmDiskFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmDiskFailedEvent.to_json()

# convert the object into a dict
vm_disk_failed_event_dict = vm_disk_failed_event_instance.to_dict()
# create an instance of VmDiskFailedEvent from a dict
vm_disk_failed_event_form_dict = vm_disk_failed_event.from_dict(vm_disk_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


