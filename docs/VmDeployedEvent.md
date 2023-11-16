# VmDeployedEvent

This event records the completion of a virtual machine deployment operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_template** | [**VmEventArgument**](VmEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.vm_deployed_event import VmDeployedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDeployedEvent from a JSON string
vm_deployed_event_instance = VmDeployedEvent.from_json(json)
# print the JSON string representation of the object
print VmDeployedEvent.to_json()

# convert the object into a dict
vm_deployed_event_dict = vm_deployed_event_instance.to_dict()
# create an instance of VmDeployedEvent from a dict
vm_deployed_event_form_dict = vm_deployed_event.from_dict(vm_deployed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


