# VMwareVspanPort

This class defines the ports, uplink ports name, vlans and IP addresses participating in a Distributed Port Mirroring session.  See *VMwareVspanSession*.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port_key** | **List[str]** | Individual ports to participate in the Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0  | [optional] 
**uplink_port_name** | **List[str]** | Uplink ports used as destination ports to participate in the Distributed Port Mirroring session.  A fault will be raised if uplinkPortName is used as source ports in any Distributed Port Mirroring session.  ***Since:*** vSphere API 5.0  | [optional] 
**wildcard_port_connectee_type** | **List[str]** | Wild card specification for source ports participating in the Distributed Port Mirroring session.  See *DistributedVirtualSwitchPortConnecteeConnecteeType_enum* for valid values. Any port that has a connectee of the specified type has its receive traffic mirrored. A fault will be raised if wildcards are specified as destination ports or source ports mirroring traffic on the transmit side. It is to be not used.  ***Since:*** vSphere API 5.0  | [optional] 
**vlans** | **List[int]** | Vlan Ids for ingress source of Remote Mirror destination session.  ***Since:*** vSphere API 5.1  | [optional] 
**ip_address** | **List[str]** | IP address for the destination of encapsulated remote mirror source session, IPv4 address is specified using dotted decimal notation.  For example, \&quot;192.0.2.1\&quot;. IPv6 addresses are 128-bit addresses represented as eight fields of up to four hexadecimal digits. A colon separates each field (:). For example, 2001:DB8:101::230:6eff:fe04:d9ff.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.v_mware_vspan_port import VMwareVspanPort

# TODO update the JSON string below
json = "{}"
# create an instance of VMwareVspanPort from a JSON string
v_mware_vspan_port_instance = VMwareVspanPort.from_json(json)
# print the JSON string representation of the object
print VMwareVspanPort.to_json()

# convert the object into a dict
v_mware_vspan_port_dict = v_mware_vspan_port_instance.to_dict()
# create an instance of VMwareVspanPort from a dict
v_mware_vspan_port_form_dict = v_mware_vspan_port.from_dict(v_mware_vspan_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


