# RollbackEvent

This event is generated when network configuration rollback occurs on a host due configuration change that disconnected the host from vSphere server  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | The host on which rollback happened  ***Since:*** vSphere API 5.1  | 
**method_name** | **str** | The API method that was rolled back  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.rollback_event import RollbackEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RollbackEvent from a JSON string
rollback_event_instance = RollbackEvent.from_json(json)
# print the JSON string representation of the object
print RollbackEvent.to_json()

# convert the object into a dict
rollback_event_dict = rollback_event_instance.to_dict()
# create an instance of RollbackEvent from a dict
rollback_event_form_dict = rollback_event.from_dict(rollback_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


