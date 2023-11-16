# QueryProviderNameRequestType

The parameters of *HealthUpdateManager.QueryProviderName*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 

## Example

```python
from vmware_vi.models.query_provider_name_request_type import QueryProviderNameRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryProviderNameRequestType from a JSON string
query_provider_name_request_type_instance = QueryProviderNameRequestType.from_json(json)
# print the JSON string representation of the object
print QueryProviderNameRequestType.to_json()

# convert the object into a dict
query_provider_name_request_type_dict = query_provider_name_request_type_instance.to_dict()
# create an instance of QueryProviderNameRequestType from a dict
query_provider_name_request_type_form_dict = query_provider_name_request_type.from_dict(query_provider_name_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


