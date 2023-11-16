# ArrayOfVmResourcePoolMovedEvent

A boxed array of *VmResourcePoolMovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VmResourcePoolMovedEvent]**](VmResourcePoolMovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vm_resource_pool_moved_event import ArrayOfVmResourcePoolMovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVmResourcePoolMovedEvent from a JSON string
array_of_vm_resource_pool_moved_event_instance = ArrayOfVmResourcePoolMovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfVmResourcePoolMovedEvent.to_json()

# convert the object into a dict
array_of_vm_resource_pool_moved_event_dict = array_of_vm_resource_pool_moved_event_instance.to_dict()
# create an instance of ArrayOfVmResourcePoolMovedEvent from a dict
array_of_vm_resource_pool_moved_event_form_dict = array_of_vm_resource_pool_moved_event.from_dict(array_of_vm_resource_pool_moved_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


