# QueryNetConfigRequestType

The parameters of *HostVirtualNicManager.QueryNetConfig*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nic_type** | **str** | The *HostVirtualNicManagerNicType_enum*  | 

## Example

```python
from vmware_vi.models.query_net_config_request_type import QueryNetConfigRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNetConfigRequestType from a JSON string
query_net_config_request_type_instance = QueryNetConfigRequestType.from_json(json)
# print the JSON string representation of the object
print QueryNetConfigRequestType.to_json()

# convert the object into a dict
query_net_config_request_type_dict = query_net_config_request_type_instance.to_dict()
# create an instance of QueryNetConfigRequestType from a dict
query_net_config_request_type_form_dict = query_net_config_request_type.from_dict(query_net_config_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


