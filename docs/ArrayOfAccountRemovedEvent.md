# ArrayOfAccountRemovedEvent

A boxed array of *AccountRemovedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[AccountRemovedEvent]**](AccountRemovedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_account_removed_event import ArrayOfAccountRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfAccountRemovedEvent from a JSON string
array_of_account_removed_event_instance = ArrayOfAccountRemovedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfAccountRemovedEvent.to_json()

# convert the object into a dict
array_of_account_removed_event_dict = array_of_account_removed_event_instance.to_dict()
# create an instance of ArrayOfAccountRemovedEvent from a dict
array_of_account_removed_event_form_dict = array_of_account_removed_event.from_dict(array_of_account_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


