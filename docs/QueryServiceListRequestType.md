# QueryServiceListRequestType

The parameters of *ServiceManager.QueryServiceList*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **str** | The name of the service to be located.  | [optional] 
**location** | **List[str]** | The list of location information that needs to match for a service to be considered a match.  | [optional] 

## Example

```python
from vmware_vi.models.query_service_list_request_type import QueryServiceListRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryServiceListRequestType from a JSON string
query_service_list_request_type_instance = QueryServiceListRequestType.from_json(json)
# print the JSON string representation of the object
print QueryServiceListRequestType.to_json()

# convert the object into a dict
query_service_list_request_type_dict = query_service_list_request_type_instance.to_dict()
# create an instance of QueryServiceListRequestType from a dict
query_service_list_request_type_form_dict = query_service_list_request_type.from_dict(query_service_list_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


