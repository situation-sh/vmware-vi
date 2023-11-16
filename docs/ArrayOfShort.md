# ArrayOfShort

A boxed array of *PrimitiveShort*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **List[int]** |  | 

## Example

```python
from vmware_vi.models.array_of_short import ArrayOfShort

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfShort from a JSON string
array_of_short_instance = ArrayOfShort.from_json(json)
# print the JSON string representation of the object
print ArrayOfShort.to_json()

# convert the object into a dict
array_of_short_dict = array_of_short_instance.to_dict()
# create an instance of ArrayOfShort from a dict
array_of_short_form_dict = array_of_short.from_dict(array_of_short_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


