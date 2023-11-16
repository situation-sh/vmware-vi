# ArrayOfEventDescriptionEventDetail

A boxed array of *EventDescriptionEventDetail*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[EventDescriptionEventDetail]**](EventDescriptionEventDetail.md) |  | 

## Example

```python
from vmware_vi.models.array_of_event_description_event_detail import ArrayOfEventDescriptionEventDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfEventDescriptionEventDetail from a JSON string
array_of_event_description_event_detail_instance = ArrayOfEventDescriptionEventDetail.from_json(json)
# print the JSON string representation of the object
print ArrayOfEventDescriptionEventDetail.to_json()

# convert the object into a dict
array_of_event_description_event_detail_dict = array_of_event_description_event_detail_instance.to_dict()
# create an instance of ArrayOfEventDescriptionEventDetail from a dict
array_of_event_description_event_detail_form_dict = array_of_event_description_event_detail.from_dict(array_of_event_description_event_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


