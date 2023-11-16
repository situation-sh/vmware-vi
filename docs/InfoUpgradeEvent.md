# InfoUpgradeEvent

This event is a general information event from upgrade. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.info_upgrade_event import InfoUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InfoUpgradeEvent from a JSON string
info_upgrade_event_instance = InfoUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print InfoUpgradeEvent.to_json()

# convert the object into a dict
info_upgrade_event_dict = info_upgrade_event_instance.to_dict()
# create an instance of InfoUpgradeEvent from a dict
info_upgrade_event_form_dict = info_upgrade_event.from_dict(info_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


