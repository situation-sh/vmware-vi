# ArrayOfInvalidRequest

A boxed array of *InvalidRequest*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[InvalidRequest]**](InvalidRequest.md) |  | 

## Example

```python
from vmware_vi.models.array_of_invalid_request import ArrayOfInvalidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfInvalidRequest from a JSON string
array_of_invalid_request_instance = ArrayOfInvalidRequest.from_json(json)
# print the JSON string representation of the object
print ArrayOfInvalidRequest.to_json()

# convert the object into a dict
array_of_invalid_request_dict = array_of_invalid_request_instance.to_dict()
# create an instance of ArrayOfInvalidRequest from a dict
array_of_invalid_request_form_dict = array_of_invalid_request.from_dict(array_of_invalid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


