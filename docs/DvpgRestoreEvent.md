# DvpgRestoreEvent

This event is generated when a restore operation is performed on a distributed virtual portgroup  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvpg_restore_event import DvpgRestoreEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvpgRestoreEvent from a JSON string
dvpg_restore_event_instance = DvpgRestoreEvent.from_json(json)
# print the JSON string representation of the object
print DvpgRestoreEvent.to_json()

# convert the object into a dict
dvpg_restore_event_dict = dvpg_restore_event_instance.to_dict()
# create an instance of DvpgRestoreEvent from a dict
dvpg_restore_event_form_dict = dvpg_restore_event.from_dict(dvpg_restore_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


