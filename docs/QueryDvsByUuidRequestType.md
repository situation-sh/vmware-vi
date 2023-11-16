# QueryDvsByUuidRequestType

The parameters of *DistributedVirtualSwitchManager.QueryDvsByUuid*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 

## Example

```python
from vmware_vi.models.query_dvs_by_uuid_request_type import QueryDvsByUuidRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryDvsByUuidRequestType from a JSON string
query_dvs_by_uuid_request_type_instance = QueryDvsByUuidRequestType.from_json(json)
# print the JSON string representation of the object
print QueryDvsByUuidRequestType.to_json()

# convert the object into a dict
query_dvs_by_uuid_request_type_dict = query_dvs_by_uuid_request_type_instance.to_dict()
# create an instance of QueryDvsByUuidRequestType from a dict
query_dvs_by_uuid_request_type_form_dict = query_dvs_by_uuid_request_type.from_dict(query_dvs_by_uuid_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


