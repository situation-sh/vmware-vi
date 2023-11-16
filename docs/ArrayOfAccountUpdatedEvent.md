# ArrayOfAccountUpdatedEvent

A boxed array of *AccountUpdatedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AccountUpdatedEvent]**](AccountUpdatedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_account_updated_event import ArrayOfAccountUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAccountUpdatedEvent from a JSON string
array_of_account_updated_event_instance = ArrayOfAccountUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAccountUpdatedEvent.to_json()

# convert the object into a dict
array_of_account_updated_event_dict = array_of_account_updated_event_instance.to_dict()
# create an instance of ArrayOfAccountUpdatedEvent from a dict
array_of_account_updated_event_form_dict = array_of_account_updated_event.from_dict(array_of_account_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


