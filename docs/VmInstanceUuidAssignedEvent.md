# VmInstanceUuidAssignedEvent

This event records the assignment of a new instance UUID to a virtual machine.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_uuid** | **str** | The new instance UUID.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_instance_uuid_assigned_event import VmInstanceUuidAssignedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmInstanceUuidAssignedEvent from a JSON string
vm_instance_uuid_assigned_event_instance = VmInstanceUuidAssignedEvent.from_json(json)
# print the JSON string representation of the object
print VmInstanceUuidAssignedEvent.to_json()

# convert the object into a dict
vm_instance_uuid_assigned_event_dict = vm_instance_uuid_assigned_event_instance.to_dict()
# create an instance of VmInstanceUuidAssignedEvent from a dict
vm_instance_uuid_assigned_event_form_dict = vm_instance_uuid_assigned_event.from_dict(vm_instance_uuid_assigned_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


