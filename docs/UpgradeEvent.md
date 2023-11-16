# UpgradeEvent

These event types represent events converted from VirtualCenter 1.x.  All upgraded events are converted to string values. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The formatted message from the upgrade.  | 

## Example

```python
from vmware_vi.models.upgrade_event import UpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeEvent from a JSON string
upgrade_event_instance = UpgradeEvent.from_json(json)
# print the JSON string representation of the object
print UpgradeEvent.to_json()

# convert the object into a dict
upgrade_event_dict = upgrade_event_instance.to_dict()
# create an instance of UpgradeEvent from a dict
upgrade_event_form_dict = upgrade_event.from_dict(upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


