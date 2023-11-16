# UserUpgradeEvent

This event is a general user event from upgrade. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.user_upgrade_event import UserUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UserUpgradeEvent from a JSON string
user_upgrade_event_instance = UserUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print UserUpgradeEvent.to_json()

# convert the object into a dict
user_upgrade_event_dict = user_upgrade_event_instance.to_dict()
# create an instance of UserUpgradeEvent from a dict
user_upgrade_event_form_dict = user_upgrade_event.from_dict(user_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


