# PrimitiveDateTime

A boxed DateTime primitive. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **datetime** |  | 

## Example

```python
from vmware_vi.models.primitive_date_time import PrimitiveDateTime

# TODO update the JSON string below
json = "{}"
# create an instance of PrimitiveDateTime from a JSON string
primitive_date_time_instance = PrimitiveDateTime.from_json(json)
# print the JSON string representation of the object
print PrimitiveDateTime.to_json()

# convert the object into a dict
primitive_date_time_dict = primitive_date_time_instance.to_dict()
# create an instance of PrimitiveDateTime from a dict
primitive_date_time_form_dict = primitive_date_time.from_dict(primitive_date_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


