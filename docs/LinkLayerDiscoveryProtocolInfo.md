# LinkLayerDiscoveryProtocolInfo

The Link Layer Discovery Protocol information.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis_id** | **str** | ChassisId represents the chassis identification for the device that transmitted the LLDP frame.  The receiving LLDP agent combines the Chassis ID and portId to represent the entity connected to the port where the frame was received.  ***Since:*** vSphere API 5.0  | 
**port_id** | **str** | This property identifies the specific port that transmitted the LLDP frame.  The receiving LLDP agent combines the Chassis ID and Port to represent the entity connected to the port where the frame was received.  ***Since:*** vSphere API 5.0  | 
**time_to_live** | **int** | It is the duration of time in seconds for which information contained in the received LLDP frame shall be valid.  If a value of zero is sent it can also identify a device that has shut down or is no longer transmitting, prompting deletion of the record from the local database.  ***Since:*** vSphere API 5.0  | 
**parameter** | [**List[KeyAnyValue]**](KeyAnyValue.md) | LLDP parameters  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.link_layer_discovery_protocol_info import LinkLayerDiscoveryProtocolInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LinkLayerDiscoveryProtocolInfo from a JSON string
link_layer_discovery_protocol_info_instance = LinkLayerDiscoveryProtocolInfo.from_json(json)
# print the JSON string representation of the object
print LinkLayerDiscoveryProtocolInfo.to_json()

# convert the object into a dict
link_layer_discovery_protocol_info_dict = link_layer_discovery_protocol_info_instance.to_dict()
# create an instance of LinkLayerDiscoveryProtocolInfo from a dict
link_layer_discovery_protocol_info_form_dict = link_layer_discovery_protocol_info.from_dict(link_layer_discovery_protocol_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


