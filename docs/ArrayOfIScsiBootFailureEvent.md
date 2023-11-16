# ArrayOfIScsiBootFailureEvent

A boxed array of *IScsiBootFailureEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[IScsiBootFailureEvent]**](IScsiBootFailureEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_i_scsi_boot_failure_event import ArrayOfIScsiBootFailureEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfIScsiBootFailureEvent from a JSON string
array_of_i_scsi_boot_failure_event_instance = ArrayOfIScsiBootFailureEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfIScsiBootFailureEvent.to_json()

# convert the object into a dict
array_of_i_scsi_boot_failure_event_dict = array_of_i_scsi_boot_failure_event_instance.to_dict()
# create an instance of ArrayOfIScsiBootFailureEvent from a dict
array_of_i_scsi_boot_failure_event_form_dict = array_of_i_scsi_boot_failure_event.from_dict(array_of_i_scsi_boot_failure_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


