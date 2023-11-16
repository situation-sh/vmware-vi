# DvsDestroyedEvent

A distributed virtual switch was destroyed.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.dvs_destroyed_event import DvsDestroyedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DvsDestroyedEvent from a JSON string
dvs_destroyed_event_instance = DvsDestroyedEvent.from_json(json)
# print the JSON string representation of the object
print DvsDestroyedEvent.to_json()

# convert the object into a dict
dvs_destroyed_event_dict = dvs_destroyed_event_instance.to_dict()
# create an instance of DvsDestroyedEvent from a dict
dvs_destroyed_event_form_dict = dvs_destroyed_event.from_dict(dvs_destroyed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


