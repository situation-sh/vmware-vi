# AccountRemovedEvent

This event records that an account was removed from a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** |  | 
**group** | **bool** |  | 

## Example

```python
from vmware_vi.models.account_removed_event import AccountRemovedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountRemovedEvent from a JSON string
account_removed_event_instance = AccountRemovedEvent.from_json(json)
# print the JSON string representation of the object
print AccountRemovedEvent.to_json()

# convert the object into a dict
account_removed_event_dict = account_removed_event_instance.to_dict()
# create an instance of AccountRemovedEvent from a dict
account_removed_event_form_dict = account_removed_event.from_dict(account_removed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


