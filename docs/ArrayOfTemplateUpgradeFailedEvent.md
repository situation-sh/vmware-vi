# ArrayOfTemplateUpgradeFailedEvent

A boxed array of *TemplateUpgradeFailedEvent*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[TemplateUpgradeFailedEvent]**](TemplateUpgradeFailedEvent.md) |  | 

## Example

```python
from vmware_vi.models.array_of_template_upgrade_failed_event import ArrayOfTemplateUpgradeFailedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfTemplateUpgradeFailedEvent from a JSON string
array_of_template_upgrade_failed_event_instance = ArrayOfTemplateUpgradeFailedEvent.from_json(json)
# print the JSON string representation of the object
print ArrayOfTemplateUpgradeFailedEvent.to_json()

# convert the object into a dict
array_of_template_upgrade_failed_event_dict = array_of_template_upgrade_failed_event_instance.to_dict()
# create an instance of ArrayOfTemplateUpgradeFailedEvent from a dict
array_of_template_upgrade_failed_event_form_dict = array_of_template_upgrade_failed_event.from_dict(array_of_template_upgrade_failed_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


