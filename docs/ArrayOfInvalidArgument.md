# ArrayOfInvalidArgument

A boxed array of *InvalidArgument*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidArgument]**](InvalidArgument.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_argument import ArrayOfInvalidArgument

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidArgument from a JSON string
array_of_invalid_argument_instance = ArrayOfInvalidArgument.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidArgument.to_json()

# convert the object into a dict
array_of_invalid_argument_dict = array_of_invalid_argument_instance.to_dict()
# create an instance of ArrayOfInvalidArgument from a dict
array_of_invalid_argument_form_dict = array_of_invalid_argument.from_dict(array_of_invalid_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


