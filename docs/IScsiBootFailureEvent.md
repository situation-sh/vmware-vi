# IScsiBootFailureEvent

Could not boot from iScsi.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.i_scsi_boot_failure_event import IScsiBootFailureEvent

# TODO update the JSON string below
json = "{}"
# create an instance of IScsiBootFailureEvent from a JSON string
i_scsi_boot_failure_event_instance = IScsiBootFailureEvent.from_json(json)
# print the JSON string representation of the object
print IScsiBootFailureEvent.to_json()

# convert the object into a dict
i_scsi_boot_failure_event_dict = i_scsi_boot_failure_event_instance.to_dict()
# create an instance of IScsiBootFailureEvent from a dict
i_scsi_boot_failure_event_form_dict = i_scsi_boot_failure_event.from_dict(i_scsi_boot_failure_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


