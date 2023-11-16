# ArrayOfInvalidHostName

A boxed array of *InvalidHostName*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidHostName]**](InvalidHostName.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_host_name import ArrayOfInvalidHostName

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidHostName from a JSON string
array_of_invalid_host_name_instance = ArrayOfInvalidHostName.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidHostName.to_json()

# convert the object into a dict
array_of_invalid_host_name_dict = array_of_invalid_host_name_instance.to_dict()
# create an instance of ArrayOfInvalidHostName from a dict
array_of_invalid_host_name_form_dict = array_of_invalid_host_name.from_dict(array_of_invalid_host_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


