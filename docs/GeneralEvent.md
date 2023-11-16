# GeneralEvent

These are general events. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A short form of the message string, not localized.  | 

## Example

```python
from vmware_vi.models.general_event import GeneralEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralEvent from a JSON string
general_event_instance = GeneralEvent.from_json(json)
# print the JSON string representation of the object
print GeneralEvent.to_json()

# convert the object into a dict
general_event_dict = general_event_instance.to_dict()
# create an instance of GeneralEvent from a dict
general_event_form_dict = general_event.from_dict(general_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


