# CustomizationStartedEvent

The customization sequence has started in the VM guest.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_started_event import CustomizationStartedEvent

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationStartedEvent from a JSON string
customization_started_event_instance = CustomizationStartedEvent.from_json(json)
# print the JSON string representation of the object
print CustomizationStartedEvent.to_json()

# convert the object into a dict
customization_started_event_dict = customization_started_event_instance.to_dict()
# create an instance of CustomizationStartedEvent from a dict
customization_started_event_form_dict = customization_started_event.from_dict(customization_started_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


