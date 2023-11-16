# InvalidArgument

An InvalidArgument exception is thrown if the set of arguments passed to the function is not specified correctly. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invalid_property** | **str** | Optional name of the invalid property.  | [optional] 

## Example

```python
from vmware_vi.models.invalid_argument import InvalidArgument

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidArgument from a JSON string
invalid_argument_instance = InvalidArgument.from_json(json)
# print the JSON string representation of the object
print InvalidArgument.to_json()

# convert the object into a dict
invalid_argument_dict = invalid_argument_instance.to_dict()
# create an instance of InvalidArgument from a dict
invalid_argument_form_dict = invalid_argument.from_dict(invalid_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


