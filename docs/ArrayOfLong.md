# ArrayOfLong

A boxed array of *PrimitiveLong*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[int]** |  | 

## Example

```python
from vmware_vi.models.array_of_long import ArrayOfLong

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLong from a JSON string
array_of_long_instance = ArrayOfLong.from_json(json)
# print the JSON string representation of the object
print ArrayOfLong.to_json()

# convert the object into a dict
array_of_long_dict = array_of_long_instance.to_dict()
# create an instance of ArrayOfLong from a dict
array_of_long_form_dict = array_of_long.from_dict(array_of_long_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


