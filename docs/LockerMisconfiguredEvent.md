# LockerMisconfiguredEvent

Locker has not been configured properly.  This event is fired when the datastore configured to back the locker does not exist or when connectivity to the datastore is lost.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | [**DatastoreEventArgument**](DatastoreEventArgument.md) |  | 

## Example

```python
from vmware_vi.models.locker_misconfigured_event import LockerMisconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LockerMisconfiguredEvent from a JSON string
locker_misconfigured_event_instance = LockerMisconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print LockerMisconfiguredEvent.to_json()

# convert the object into a dict
locker_misconfigured_event_dict = locker_misconfigured_event_instance.to_dict()
# create an instance of LockerMisconfiguredEvent from a dict
locker_misconfigured_event_form_dict = locker_misconfigured_event.from_dict(locker_misconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


