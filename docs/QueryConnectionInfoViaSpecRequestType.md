# QueryConnectionInfoViaSpecRequestType

The parameters of *Datacenter.QueryConnectionInfoViaSpec*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**HostConnectSpec**](HostConnectSpec.md) |  | 

## Example

```python
from vmware_vi.models.query_connection_info_via_spec_request_type import QueryConnectionInfoViaSpecRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryConnectionInfoViaSpecRequestType from a JSON string
query_connection_info_via_spec_request_type_instance = QueryConnectionInfoViaSpecRequestType.from_json(json)
# print the JSON string representation of the object
print QueryConnectionInfoViaSpecRequestType.to_json()

# convert the object into a dict
query_connection_info_via_spec_request_type_dict = query_connection_info_via_spec_request_type_instance.to_dict()
# create an instance of QueryConnectionInfoViaSpecRequestType from a dict
query_connection_info_via_spec_request_type_form_dict = query_connection_info_via_spec_request_type.from_dict(query_connection_info_via_spec_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


