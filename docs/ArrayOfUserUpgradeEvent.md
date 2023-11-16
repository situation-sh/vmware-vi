# ArrayOfUserUpgradeEvent

A boxed array of *UserUpgradeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[UserUpgradeEvent]**](UserUpgradeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_user_upgrade_event import ArrayOfUserUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUserUpgradeEvent from a JSON string
array_of_user_upgrade_event_instance = ArrayOfUserUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfUserUpgradeEvent.to_json()

# convert the object into a dict
array_of_user_upgrade_event_dict = array_of_user_upgrade_event_instance.to_dict()
# create an instance of ArrayOfUserUpgradeEvent from a dict
array_of_user_upgrade_event_form_dict = array_of_user_upgrade_event.from_dict(array_of_user_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


