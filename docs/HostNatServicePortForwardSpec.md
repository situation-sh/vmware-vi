# HostNatServicePortForwardSpec

This data object type describes the Network Address Translation (NAT) port forwarding specification.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Either \&quot;tcp\&quot; or \&quot;udp\&quot;.  ***Since:*** VI API 2.5  | 
**name** | **str** | The user-defined name to identify the service being forwarded.  No white spaces are allowed in the string.  ***Since:*** VI API 2.5  | 
**host_port** | **int** | The port number on the host.  Network traffic sent to the host on this TCP/UDP port is forwarded to the guest at the specified IP address and port.  ***Since:*** VI API 2.5  | 
**guest_port** | **int** | The port number for the guest.  Network traffic from the host is forwarded to this port.  ***Since:*** VI API 2.5  | 
**guest_ip_address** | **str** | The IP address for the guest.  Network traffic from the host is forwarded to this IP address.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_nat_service_port_forward_spec import HostNatServicePortForwardSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNatServicePortForwardSpec from a JSON string
host_nat_service_port_forward_spec_instance = HostNatServicePortForwardSpec.from_json(json)
# print the JSON string representation of the object
print HostNatServicePortForwardSpec.to_json()

# convert the object into a dict
host_nat_service_port_forward_spec_dict = host_nat_service_port_forward_spec_instance.to_dict()
# create an instance of HostNatServicePortForwardSpec from a dict
host_nat_service_port_forward_spec_form_dict = host_nat_service_port_forward_spec.from_dict(host_nat_service_port_forward_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


