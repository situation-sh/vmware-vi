# InvalidEditionEvent

This event records if the edition is set to an invalid value.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature** | **str** |  | 

## Example

```python
from vmware_vi.models.invalid_edition_event import InvalidEditionEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidEditionEvent from a JSON string
invalid_edition_event_instance = InvalidEditionEvent.from_json(json)
# print the JSON string representation of the object
print InvalidEditionEvent.to_json()

# convert the object into a dict
invalid_edition_event_dict = invalid_edition_event_instance.to_dict()
# create an instance of InvalidEditionEvent from a dict
invalid_edition_event_form_dict = invalid_edition_event.from_dict(invalid_edition_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


