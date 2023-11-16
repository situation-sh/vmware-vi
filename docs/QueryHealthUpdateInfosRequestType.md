# QueryHealthUpdateInfosRequestType

The parameters of *HealthUpdateManager.QueryHealthUpdateInfos*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The provider id.  | 

## Example

```python
from vmware_vi.models.query_health_update_infos_request_type import QueryHealthUpdateInfosRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryHealthUpdateInfosRequestType from a JSON string
query_health_update_infos_request_type_instance = QueryHealthUpdateInfosRequestType.from_json(json)
# print the JSON string representation of the object
print QueryHealthUpdateInfosRequestType.to_json()

# convert the object into a dict
query_health_update_infos_request_type_dict = query_health_update_infos_request_type_instance.to_dict()
# create an instance of QueryHealthUpdateInfosRequestType from a dict
query_health_update_infos_request_type_form_dict = query_health_update_infos_request_type.from_dict(query_health_update_infos_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


