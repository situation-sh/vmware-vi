# VmInstanceUuidChangedEvent

This event records a change in a virtual machine's instance UUID.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_instance_uuid** | **str** | The old instance UUID.  ***Since:*** vSphere API 4.0  | 
**new_instance_uuid** | **str** | The new instance UUID.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_instance_uuid_changed_event import VmInstanceUuidChangedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmInstanceUuidChangedEvent from a JSON string
vm_instance_uuid_changed_event_instance = VmInstanceUuidChangedEvent.from_json(json)
# print the JSON string representation of the object
print VmInstanceUuidChangedEvent.to_json()

# convert the object into a dict
vm_instance_uuid_changed_event_dict = vm_instance_uuid_changed_event_instance.to_dict()
# create an instance of VmInstanceUuidChangedEvent from a dict
vm_instance_uuid_changed_event_form_dict = vm_instance_uuid_changed_event.from_dict(vm_instance_uuid_changed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


