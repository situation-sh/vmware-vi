# ArrayOfRequestCanceled

A boxed array of *RequestCanceled*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[RequestCanceled]**](RequestCanceled.md) |  | 

## Example

```python
from vmware_vi.models.array_of_request_canceled import ArrayOfRequestCanceled

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfRequestCanceled from a JSON string
array_of_request_canceled_instance = ArrayOfRequestCanceled.from_json(json)
# print the JSON string representation of the object
print ArrayOfRequestCanceled.to_json()

# convert the object into a dict
array_of_request_canceled_dict = array_of_request_canceled_instance.to_dict()
# create an instance of ArrayOfRequestCanceled from a dict
array_of_request_canceled_form_dict = array_of_request_canceled.from_dict(array_of_request_canceled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


