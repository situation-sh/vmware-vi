# ArrayOfWeekOfMonth

A boxed array of *WeekOfMonth_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[WeekOfMonthEnum]**](WeekOfMonthEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_week_of_month import ArrayOfWeekOfMonth

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfWeekOfMonth from a JSON string
array_of_week_of_month_instance = ArrayOfWeekOfMonth.from_json(json)
# print the JSON string representation of the object
print ArrayOfWeekOfMonth.to_json()

# convert the object into a dict
array_of_week_of_month_dict = array_of_week_of_month_instance.to_dict()
# create an instance of ArrayOfWeekOfMonth from a dict
array_of_week_of_month_form_dict = array_of_week_of_month.from_dict(array_of_week_of_month_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


