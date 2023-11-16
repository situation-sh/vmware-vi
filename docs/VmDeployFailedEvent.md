# VmDeployFailedEvent

This event records a failure to deploy from a template. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_datastore** | [**EntityEventArgument**](EntityEventArgument.md) |  | 
**reason** | [**MethodFault**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.vm_deploy_failed_event import VmDeployFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDeployFailedEvent from a JSON string
vm_deploy_failed_event_instance = VmDeployFailedEvent.from_json(json)
# print the JSON string representation of the object
print VmDeployFailedEvent.to_json()

# convert the object into a dict
vm_deploy_failed_event_dict = vm_deploy_failed_event_instance.to_dict()
# create an instance of VmDeployFailedEvent from a dict
vm_deploy_failed_event_form_dict = vm_deploy_failed_event.from_dict(vm_deploy_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


