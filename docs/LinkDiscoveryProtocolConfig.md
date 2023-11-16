# LinkDiscoveryProtocolConfig

Dataobject representing the link discovery protocol configuration for a virtual or distributed virtual switch.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | The discovery protocol type.  For valid values see *LinkDiscoveryProtocolConfigProtocolType_enum*.  ***Since:*** vSphere API 4.0  | 
**operation** | **str** | Whether to advertise or listen.  For valid values see *LinkDiscoveryProtocolConfigOperationType_enum*.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.link_discovery_protocol_config import LinkDiscoveryProtocolConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LinkDiscoveryProtocolConfig from a JSON string
link_discovery_protocol_config_instance = LinkDiscoveryProtocolConfig.from_json(json)
# print the JSON string representation of the object
print LinkDiscoveryProtocolConfig.to_json()

# convert the object into a dict
link_discovery_protocol_config_dict = link_discovery_protocol_config_instance.to_dict()
# create an instance of LinkDiscoveryProtocolConfig from a dict
link_discovery_protocol_config_form_dict = link_discovery_protocol_config.from_dict(link_discovery_protocol_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


