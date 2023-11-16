# AccountCreatedEvent

This event records that an account was created on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostAccountSpec**](HostAccountSpec.md) |  | 
**group** | **bool** |  | 

## Example

```python
from vmware_vi.models.account_created_event import AccountCreatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountCreatedEvent from a JSON string
account_created_event_instance = AccountCreatedEvent.from_json(json)
# print the JSON string representation of the object
print AccountCreatedEvent.to_json()

# convert the object into a dict
account_created_event_dict = account_created_event_instance.to_dict()
# create an instance of AccountCreatedEvent from a dict
account_created_event_form_dict = account_created_event.from_dict(account_created_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


