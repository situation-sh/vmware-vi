# NotEnoughResourcesToStartVmEvent

This event records when the HA does not find sufficient resources to failover a virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason why the virtual machine could not be restarted  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.not_enough_resources_to_start_vm_event import NotEnoughResourcesToStartVmEvent

# TODO update the JSON string below
json = "{}"
# create an instance of NotEnoughResourcesToStartVmEvent from a JSON string
not_enough_resources_to_start_vm_event_instance = NotEnoughResourcesToStartVmEvent.from_json(json)
# print the JSON string representation of the object
print NotEnoughResourcesToStartVmEvent.to_json()

# convert the object into a dict
not_enough_resources_to_start_vm_event_dict = not_enough_resources_to_start_vm_event_instance.to_dict()
# create an instance of NotEnoughResourcesToStartVmEvent from a dict
not_enough_resources_to_start_vm_event_form_dict = not_enough_resources_to_start_vm_event.from_dict(not_enough_resources_to_start_vm_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


