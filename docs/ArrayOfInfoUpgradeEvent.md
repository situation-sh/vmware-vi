# ArrayOfInfoUpgradeEvent

A boxed array of *InfoUpgradeEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InfoUpgradeEvent]**](InfoUpgradeEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_info_upgrade_event import ArrayOfInfoUpgradeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInfoUpgradeEvent from a JSON string
array_of_info_upgrade_event_instance = ArrayOfInfoUpgradeEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfInfoUpgradeEvent.to_json()

# convert the object into a dict
array_of_info_upgrade_event_dict = array_of_info_upgrade_event_instance.to_dict()
# create an instance of ArrayOfInfoUpgradeEvent from a dict
array_of_info_upgrade_event_form_dict = array_of_info_upgrade_event.from_dict(array_of_info_upgrade_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


