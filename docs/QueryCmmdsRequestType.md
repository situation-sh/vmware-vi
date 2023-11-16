# QueryCmmdsRequestType

The parameters of *HostVsanInternalSystem.QueryCmmds*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[HostVsanInternalSystemCmmdsQuery]**](HostVsanInternalSystemCmmdsQuery.md) | List of CMMDS query specs.  ***Since:*** vSphere API 5.5  | 

## Example

```python
from vmware_vi.models.query_cmmds_request_type import QueryCmmdsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryCmmdsRequestType from a JSON string
query_cmmds_request_type_instance = QueryCmmdsRequestType.from_json(json)
# print the JSON string representation of the object
print QueryCmmdsRequestType.to_json()

# convert the object into a dict
query_cmmds_request_type_dict = query_cmmds_request_type_instance.to_dict()
# create an instance of QueryCmmdsRequestType from a dict
query_cmmds_request_type_form_dict = query_cmmds_request_type.from_dict(query_cmmds_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


