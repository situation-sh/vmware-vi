# AccountUpdatedEvent

This event records that an account was updated on a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostAccountSpec**](HostAccountSpec.md) |  | 
**group** | **bool** |  | 
**prev_description** | **str** | The previous account description  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.account_updated_event import AccountUpdatedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AccountUpdatedEvent from a JSON string
account_updated_event_instance = AccountUpdatedEvent.from_json(json)
# print the JSON string representation of the object
print AccountUpdatedEvent.to_json()

# convert the object into a dict
account_updated_event_dict = account_updated_event_instance.to_dict()
# create an instance of AccountUpdatedEvent from a dict
account_updated_event_form_dict = account_updated_event.from_dict(account_updated_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


