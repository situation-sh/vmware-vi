# WarningUpgradeEvent

This event is a general warning event from upgrade. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.warning_upgrade_event import WarningUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of WarningUpgradeEvent from a JSON string
warning_upgrade_event_instance = WarningUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print WarningUpgradeEvent.to_json()

# convert the object into a dict
warning_upgrade_event_dict = warning_upgrade_event_instance.to_dict()
# create an instance of WarningUpgradeEvent from a dict
warning_upgrade_event_form_dict = warning_upgrade_event.from_dict(warning_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


