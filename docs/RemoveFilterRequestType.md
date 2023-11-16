# RemoveFilterRequestType

The parameters of *HealthUpdateManager.RemoveFilter*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | The filter id.  | 

## Example

```python
from vmware_vi.models.remove_filter_request_type import RemoveFilterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFilterRequestType from a JSON string
remove_filter_request_type_instance = RemoveFilterRequestType.from_json(json)
# print the JSON string representation of the object
print RemoveFilterRequestType.to_json()

# convert the object into a dict
remove_filter_request_type_dict = remove_filter_request_type_instance.to_dict()
# create an instance of RemoveFilterRequestType from a dict
remove_filter_request_type_form_dict = remove_filter_request_type.from_dict(remove_filter_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


