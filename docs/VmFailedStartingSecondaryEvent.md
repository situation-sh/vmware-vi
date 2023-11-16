# VmFailedStartingSecondaryEvent

This event records vmotion failure when starting a secondary VM.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | The reason for the failure.  See *VmFailedStartingSecondaryEventFailureReason_enum*  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_failed_starting_secondary_event import VmFailedStartingSecondaryEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedStartingSecondaryEvent from a JSON string
vm_failed_starting_secondary_event_instance = VmFailedStartingSecondaryEvent.from_json(json)
# print the JSON string representation of the object
print VmFailedStartingSecondaryEvent.to_json()

# convert the object into a dict
vm_failed_starting_secondary_event_dict = vm_failed_starting_secondary_event_instance.to_dict()
# create an instance of VmFailedStartingSecondaryEvent from a dict
vm_failed_starting_secondary_event_form_dict = vm_failed_starting_secondary_event.from_dict(vm_failed_starting_secondary_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


