# ArrayOfLockerMisconfiguredEvent

A boxed array of *LockerMisconfiguredEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LockerMisconfiguredEvent]**](LockerMisconfiguredEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_locker_misconfigured_event import ArrayOfLockerMisconfiguredEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLockerMisconfiguredEvent from a JSON string
array_of_locker_misconfigured_event_instance = ArrayOfLockerMisconfiguredEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfLockerMisconfiguredEvent.to_json()

# convert the object into a dict
array_of_locker_misconfigured_event_dict = array_of_locker_misconfigured_event_instance.to_dict()
# create an instance of ArrayOfLockerMisconfiguredEvent from a dict
array_of_locker_misconfigured_event_form_dict = array_of_locker_misconfigured_event.from_dict(array_of_locker_misconfigured_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


