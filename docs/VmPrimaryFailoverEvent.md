# VmPrimaryFailoverEvent

This event records a fault tolerance failover.  The reason could be : lost connection to primary, partial hardware failure of primary or by user.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  see *VirtualMachineNeedSecondaryReason_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_primary_failover_event import VmPrimaryFailoverEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmPrimaryFailoverEvent from a JSON string
vm_primary_failover_event_instance = VmPrimaryFailoverEvent.from_json(json)
# print the JSON string representation of the object
print VmPrimaryFailoverEvent.to_json()

# convert the object into a dict
vm_primary_failover_event_dict = vm_primary_failover_event_instance.to_dict()
# create an instance of VmPrimaryFailoverEvent from a dict
vm_primary_failover_event_form_dict = vm_primary_failover_event.from_dict(vm_primary_failover_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


