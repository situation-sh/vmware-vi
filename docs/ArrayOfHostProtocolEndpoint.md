# ArrayOfHostProtocolEndpoint

A boxed array of *HostProtocolEndpoint*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostProtocolEndpoint]**](HostProtocolEndpoint.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_protocol_endpoint import ArrayOfHostProtocolEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostProtocolEndpoint from a JSON string
array_of_host_protocol_endpoint_instance = ArrayOfHostProtocolEndpoint.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostProtocolEndpoint.to_json()

# convert the object into a dict
array_of_host_protocol_endpoint_dict = array_of_host_protocol_endpoint_instance.to_dict()
# create an instance of ArrayOfHostProtocolEndpoint from a dict
array_of_host_protocol_endpoint_form_dict = array_of_host_protocol_endpoint.from_dict(array_of_host_protocol_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


