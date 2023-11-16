# QueryNetworkHintRequestType

The parameters of *HostNetworkSystem.QueryNetworkHint*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **List[str]** |  | [optional] 

## Example

```python
from vmware_vi.models.query_network_hint_request_type import QueryNetworkHintRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of QueryNetworkHintRequestType from a JSON string
query_network_hint_request_type_instance = QueryNetworkHintRequestType.from_json(json)
# print the JSON string representation of the object
print QueryNetworkHintRequestType.to_json()

# convert the object into a dict
query_network_hint_request_type_dict = query_network_hint_request_type_instance.to_dict()
# create an instance of QueryNetworkHintRequestType from a dict
query_network_hint_request_type_form_dict = query_network_hint_request_type.from_dict(query_network_hint_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


