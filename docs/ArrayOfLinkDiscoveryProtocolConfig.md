# ArrayOfLinkDiscoveryProtocolConfig

A boxed array of *LinkDiscoveryProtocolConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[LinkDiscoveryProtocolConfig]**](LinkDiscoveryProtocolConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_link_discovery_protocol_config import ArrayOfLinkDiscoveryProtocolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfLinkDiscoveryProtocolConfig from a JSON string
array_of_link_discovery_protocol_config_instance = ArrayOfLinkDiscoveryProtocolConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfLinkDiscoveryProtocolConfig.to_json()

# convert the object into a dict
array_of_link_discovery_protocol_config_dict = array_of_link_discovery_protocol_config_instance.to_dict()
# create an instance of ArrayOfLinkDiscoveryProtocolConfig from a dict
array_of_link_discovery_protocol_config_form_dict = array_of_link_discovery_protocol_config.from_dict(array_of_link_discovery_protocol_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


