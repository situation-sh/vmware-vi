# BatchQueryConnectInfoRequestType

The parameters of *Datacenter.BatchQueryConnectInfo*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_specs** | [**List[HostConnectSpec]**](HostConnectSpec.md) | Information about the set of hosts to query.  | [optional] 

## Example

```python
from vmware_vi.models.batch_query_connect_info_request_type import BatchQueryConnectInfoRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of BatchQueryConnectInfoRequestType from a JSON string
batch_query_connect_info_request_type_instance = BatchQueryConnectInfoRequestType.from_json(json)
# print the JSON string representation of the object
print BatchQueryConnectInfoRequestType.to_json()

# convert the object into a dict
batch_query_connect_info_request_type_dict = batch_query_connect_info_request_type_instance.to_dict()
# create an instance of BatchQueryConnectInfoRequestType from a dict
batch_query_connect_info_request_type_form_dict = batch_query_connect_info_request_type.from_dict(batch_query_connect_info_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


