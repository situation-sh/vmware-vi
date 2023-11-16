# ArrayOfDateTime

A boxed array of *PrimitiveDateTime*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[datetime]** |  | 

## Example

```python
from vmware_vi.models.array_of_date_time import ArrayOfDateTime

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfDateTime from a JSON string
array_of_date_time_instance = ArrayOfDateTime.from_json(json)
# print the JSON string representation of the object
print ArrayOfDateTime.to_json()

# convert the object into a dict
array_of_date_time_dict = array_of_date_time_instance.to_dict()
# create an instance of ArrayOfDateTime from a dict
array_of_date_time_form_dict = array_of_date_time.from_dict(array_of_date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


