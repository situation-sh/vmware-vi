# InvalidIndexArgument

An InvalidIndexArgument exception is thrown if the index was not found  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Value of index that was not found  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.invalid_index_argument import InvalidIndexArgument

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidIndexArgument from a JSON string
invalid_index_argument_instance = InvalidIndexArgument.from_json(json)
# print the JSON string representation of the object
print InvalidIndexArgument.to_json()

# convert the object into a dict
invalid_index_argument_dict = invalid_index_argument_instance.to_dict()
# create an instance of InvalidIndexArgument from a dict
invalid_index_argument_form_dict = invalid_index_argument.from_dict(invalid_index_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


