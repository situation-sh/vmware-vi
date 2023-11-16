# VmSecondaryDisabledBySystemEvent

This event records that a fault tolerance secondary VM has been disabled by vCenter because the VM could not be powered on.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | [**MethodFault**](MethodFault.md) |  | [optional] 

## Example

```python
from vmware_vi.models.vm_secondary_disabled_by_system_event import VmSecondaryDisabledBySystemEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmSecondaryDisabledBySystemEvent from a JSON string
vm_secondary_disabled_by_system_event_instance = VmSecondaryDisabledBySystemEvent.from_json(json)
# print the JSON string representation of the object
print VmSecondaryDisabledBySystemEvent.to_json()

# convert the object into a dict
vm_secondary_disabled_by_system_event_dict = vm_secondary_disabled_by_system_event_instance.to_dict()
# create an instance of VmSecondaryDisabledBySystemEvent from a dict
vm_secondary_disabled_by_system_event_form_dict = vm_secondary_disabled_by_system_event.from_dict(vm_secondary_disabled_by_system_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


