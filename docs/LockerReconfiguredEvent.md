# LockerReconfiguredEvent

Locker was reconfigured to a new location.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 
**new_datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | [optional] 

## Example

```python
from vmware_vi.models.locker_reconfigured_event import LockerReconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LockerReconfiguredEvent from a JSON string
locker_reconfigured_event_instance = LockerReconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print LockerReconfiguredEvent.to_json()

# convert the object into a dict
locker_reconfigured_event_dict = locker_reconfigured_event_instance.to_dict()
# create an instance of LockerReconfiguredEvent from a dict
locker_reconfigured_event_form_dict = locker_reconfigured_event.from_dict(locker_reconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


