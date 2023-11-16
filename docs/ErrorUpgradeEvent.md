# ErrorUpgradeEvent

This event is a general error event from upgrade. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.error_upgrade_event import ErrorUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorUpgradeEvent from a JSON string
error_upgrade_event_instance = ErrorUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print ErrorUpgradeEvent.to_json()

# convert the object into a dict
error_upgrade_event_dict = error_upgrade_event_instance.to_dict()
# create an instance of ErrorUpgradeEvent from a dict
error_upgrade_event_form_dict = error_upgrade_event.from_dict(error_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


