# ArrayOfWarningUpgradeEvent

A boxed array of *WarningUpgradeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[WarningUpgradeEvent]**](WarningUpgradeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_warning_upgrade_event import ArrayOfWarningUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfWarningUpgradeEvent from a JSON string
array_of_warning_upgrade_event_instance = ArrayOfWarningUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfWarningUpgradeEvent.to_json()

# convert the object into a dict
array_of_warning_upgrade_event_dict = array_of_warning_upgrade_event_instance.to_dict()
# create an instance of ArrayOfWarningUpgradeEvent from a dict
array_of_warning_upgrade_event_form_dict = array_of_warning_upgrade_event.from_dict(array_of_warning_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


