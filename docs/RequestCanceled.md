# RequestCanceled

A RequestCanceled fault is thrown if the user canceled the task. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.request_canceled import RequestCanceled

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCanceled from a JSON string
request_canceled_instance = RequestCanceled.from_json(json)
# print the JSON string representation of the object
print RequestCanceled.to_json()

# convert the object into a dict
request_canceled_dict = request_canceled_instance.to_dict()
# create an instance of RequestCanceled from a dict
request_canceled_form_dict = request_canceled.from_dict(request_canceled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


