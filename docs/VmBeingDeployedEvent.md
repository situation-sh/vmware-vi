# VmBeingDeployedEvent

This event records a virtual machine being deployed from a template. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_template** | [**VmEventArgument**](VmEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_being_deployed_event import VmBeingDeployedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmBeingDeployedEvent from a JSON string
vm_being_deployed_event_instance = VmBeingDeployedEvent.from_json(json)
# print the JSON string representation of the object
print VmBeingDeployedEvent.to_json()

# convert the object into a dict
vm_being_deployed_event_dict = vm_being_deployed_event_instance.to_dict()
# create an instance of VmBeingDeployedEvent from a dict
vm_being_deployed_event_form_dict = vm_being_deployed_event.from_dict(vm_being_deployed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


