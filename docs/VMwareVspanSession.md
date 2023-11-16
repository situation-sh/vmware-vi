# VMwareVspanSession

The *VMwareVspanSession* data object defines the configuration of a VLAN Services and Protocols for Advanced Networks (VSPAN) session.  You use a VSPAN session for the following operations: - To mirror network traffic (inbound/outbound) from a set of source   entities to a set of destination entities. - To assist in troubleshooting. - As input for security and other network analysis appliances.    The type of entities that you can specify as source or destination is determined by the session type. You can use uplink distributed virtual ports only for mixed destination mirror VSPAN sessions (mixedDestMirror). For all sessions except mixedDestMirror sessions, you cannot use uplink distributed virtual ports as destination ports. sessionType is required for vSphere Distributed Switch 5.1 and later, ignored for prior version if set. <table> <thead> <tr> <th>Session Type</th> <th>Source</th> <th>Destination </th> </tr> </thead> <tbody> <tr> <td>mixedDestMirror</td> <td>Distributed Ports</td> <td>Distributed Ports + Uplink Ports Name</td> </tr> <tr> <td>dvPortMirror</td> <td>Distributed Ports</td> <td>Distributed Ports</td> </tr> <tr> <td>remoteMirrorSource</td> <td>Distributed Ports</td> <td>Uplink Ports Name</td> </tr> <tr> <td>remoteMirrorDest</td> <td>VLAN</td> <td>Distributed Ports</td> </tr> <tr> <td>encapRemoteMirrorSource</td> <td>Distributed Ports</td> <td>IP address</td> </tr> </tbody> </table>  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The generated key as the identifier for the session.  ***Since:*** vSphere API 5.0  | [optional] 
**name** | **str** | The display name.  ***Since:*** vSphere API 5.0  | [optional] 
**description** | **str** | The description for the session.  ***Since:*** vSphere API 5.0  | [optional] 
**enabled** | **bool** | Whether the session is enabled.  ***Since:*** vSphere API 5.0  | 
**source_port_transmitted** | [**VMwareVspanPort**](VMwareVspanPort.md) |  | [optional] 
**source_port_received** | [**VMwareVspanPort**](VMwareVspanPort.md) |  | [optional] 
**destination_port** | [**VMwareVspanPort**](VMwareVspanPort.md) |  | [optional] 
**encapsulation_vlan_id** | **int** | VLAN ID used to encapsulate the mirrored traffic.  ***Since:*** vSphere API 5.0  | [optional] 
**strip_original_vlan** | **bool** | Whether to strip the original VLAN tag.  if false, the original VLAN tag will be preserved on the mirrored traffic. If *VMwareVspanSession.encapsulationVlanId* has been set and this property is false, the frames will be double tagged with the original VLAN ID as the inner tag.  ***Since:*** vSphere API 5.0  | 
**mirrored_packet_length** | **int** | An integer that describes how much of each frame to mirror.  If unset, all of the frame would be mirrored. Setting this property to a smaller value is useful when the consumer will look only at the headers. The value cannot be less than 60.  ***Since:*** vSphere API 5.0  | [optional] 
**normal_traffic_allowed** | **bool** | Whether or not destination ports can send and receive \&quot;normal\&quot; traffic.  Setting this to false will make mirror ports be used solely for mirroring and not double as normal access ports.  ***Since:*** vSphere API 5.0  | 
**session_type** | **str** | Type of the session.  See *VMwareDVSVspanSessionType_enum* for valid values. Default value is mixedDestMirror if unspecified in a VSPAN create operation.  ***Since:*** vSphere API 5.1  | [optional] 
**sampling_rate** | **int** | Sampling rate of the session.  If its value is n, one of every n packets is mirrored. Valid values are between 1 to 65535, and default value is 1.  ***Since:*** vSphere API 5.1  | [optional] 
**encap_type** | **str** | Encapsulation type of the session.  See *VMwareDVSVspanSessionEncapType_enum* for valid values. Default value is encapProtocolGRE if unspecified in a VSPAN create operation.  ***Since:*** vSphere API 6.5  | [optional] 
**erspan_id** | **int** | ERSPAN ID of the session.  Valid values are between 0 to 0x3ff, and default value is 0. This value is applicable only if encaptType is *erspan2* or *erspan3*  ***Since:*** vSphere API 6.5  | [optional] 
**erspan_cos** | **int** | Class of Service of the monitored frame.  Valid values are between 0 to 7, and default value is 0. This value is applicable only if encaptType is *erspan2* or *erspan3*  ***Since:*** vSphere API 6.5  | [optional] 
**erspan_gra_nanosec** | **bool** | Timestamp Granularity.  If the value is false, timestamp-granularity will be microsecond. Otherwise the timestamp-granularity will be nanosecond This value is applicable only if encaptType is *erspan3*  ***Since:*** vSphere API 6.5  | [optional] 
**netstack** | **str** | Netstack instance of the session.  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_vspan_session import VMwareVspanSession

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareVspanSession from a JSON string
v_mware_vspan_session_instance = VMwareVspanSession.from_json(json)
# print the JSON string representation of the object
print VMwareVspanSession.to_json()

# convert the object into a dict
v_mware_vspan_session_dict = v_mware_vspan_session_instance.to_dict()
# create an instance of VMwareVspanSession from a dict
v_mware_vspan_session_form_dict = v_mware_vspan_session.from_dict(v_mware_vspan_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


