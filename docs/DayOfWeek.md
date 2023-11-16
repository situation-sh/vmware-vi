# DayOfWeek

A boxed *DayOfWeek_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**DayOfWeekEnum**](DayOfWeekEnum.md) |  | 

## Example

```python
from vmware_vi.models.day_of_week import DayOfWeek

# TODO update the JSON string below
json = "{}"
# create an instance of DayOfWeek from a JSON string
day_of_week_instance = DayOfWeek.from_json(json)
# print the JSON string representation of the object
print DayOfWeek.to_json()

# convert the object into a dict
day_of_week_dict = day_of_week_instance.to_dict()
# create an instance of DayOfWeek from a dict
day_of_week_form_dict = day_of_week.from_dict(day_of_week_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


