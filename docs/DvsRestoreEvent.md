# DvsRestoreEvent

This event is generated when a restore operation is performed on a distributed virtual switch  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_restore_event import DvsRestoreEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsRestoreEvent from a JSON string
dvs_restore_event_instance = DvsRestoreEvent.from_json(json)
# print the JSON string representation of the object
print DvsRestoreEvent.to_json()

# convert the object into a dict
dvs_restore_event_dict = dvs_restore_event_instance.to_dict()
# create an instance of DvsRestoreEvent from a dict
dvs_restore_event_form_dict = dvs_restore_event.from_dict(dvs_restore_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


