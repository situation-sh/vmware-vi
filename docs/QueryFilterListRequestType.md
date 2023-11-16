# QueryFilterListRequestType

The parameters of *HealthUpdateManager.QueryFilterList*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 

## Example

```python
from vmware_vi.models.query_filter_list_request_type import QueryFilterListRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilterListRequestType from a JSON string
query_filter_list_request_type_instance = QueryFilterListRequestType.from_json(json)
# print the JSON string representation of the object
print QueryFilterListRequestType.to_json()

# convert the object into a dict
query_filter_list_request_type_dict = query_filter_list_request_type_instance.to_dict()
# create an instance of QueryFilterListRequestType from a dict
query_filter_list_request_type_form_dict = query_filter_list_request_type.from_dict(query_filter_list_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


