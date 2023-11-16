# WeekOfMonth

A boxed *WeekOfMonth_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**WeekOfMonthEnum**](WeekOfMonthEnum.md) |  | 

## Example

```python
from vmware_vi.models.week_of_month import WeekOfMonth

# TODO update the JSON string below
json = "{}"
# create an instance of WeekOfMonth from a JSON string
week_of_month_instance = WeekOfMonth.from_json(json)
# print the JSON string representation of the object
print WeekOfMonth.to_json()

# convert the object into a dict
week_of_month_dict = week_of_month_instance.to_dict()
# create an instance of WeekOfMonth from a dict
week_of_month_form_dict = week_of_month.from_dict(week_of_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


