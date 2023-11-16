# EventDescription

This data object provides static, locale-specific strings for event objects. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | [**List[ElementDescription]**](ElementDescription.md) | *Event Category enum*  | 
**event_info** | [**List[EventDescriptionEventDetail]**](EventDescriptionEventDetail.md) | The event class description details.  | 
**enumerated_types** | [**List[EnumDescription]**](EnumDescription.md) | Localized descriptions of all enumerated types that are used for member declarations in event classes.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.event_description import EventDescription

# TODO update the JSON string below
json = "{}"
# create an instance of EventDescription from a JSON string
event_description_instance = EventDescription.from_json(json)
# print the JSON string representation of the object
print EventDescription.to_json()

# convert the object into a dict
event_description_dict = event_description_instance.to_dict()
# create an instance of EventDescription from a dict
event_description_form_dict = event_description.from_dict(event_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


