# VmResourcePoolMovedEvent

This event records when a virtual machine is moved from one resource pool to another. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_parent** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 
**new_parent** | [**ResourcePoolEventArgument**](ResourcePoolEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_resource_pool_moved_event import VmResourcePoolMovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmResourcePoolMovedEvent from a JSON string
vm_resource_pool_moved_event_instance = VmResourcePoolMovedEvent.from_json(json)
# print the JSON string representation of the object
print VmResourcePoolMovedEvent.to_json()

# convert the object into a dict
vm_resource_pool_moved_event_dict = vm_resource_pool_moved_event_instance.to_dict()
# create an instance of VmResourcePoolMovedEvent from a dict
vm_resource_pool_moved_event_form_dict = vm_resource_pool_moved_event.from_dict(vm_resource_pool_moved_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


