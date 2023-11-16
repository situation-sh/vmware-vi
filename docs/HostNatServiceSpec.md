# HostNatServiceSpec

This data object type provides the details about the Network Address Translation (NAT) service.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_switch** | **str** | The name of the virtual switch to which nat service is connected.  ***Since:*** VI API 2.5  | 
**active_ftp** | **bool** | The flag to indicate whether or not non-passive mode FTP connections should be allowed.  ***Since:*** VI API 2.5  | 
**allow_any_oui** | **bool** | The flag to indicate whether or not the NAT Service allows media access control traffic from any Organizational Unique Identifier (OUI)? By default, it does not allow traffic that originated from the host to avoid packet loops.  ***Since:*** VI API 2.5  | 
**config_port** | **bool** | The flag to indicate whether or not the NAT Service should open a configuration port.  ***Since:*** VI API 2.5  | 
**ip_gateway_address** | **str** | The IP address that the NAT Service should use on the virtual network.  ***Since:*** VI API 2.5  | 
**udp_timeout** | **int** | The time allotted for UDP packets.  ***Since:*** VI API 2.5  | 
**port_forward** | [**List[HostNatServicePortForwardSpec]**](HostNatServicePortForwardSpec.md) | The port forwarding specifications to allow network connections to be initiated from outside the firewall.  ***Since:*** VI API 2.5  | [optional] 
**name_service** | [**HostNatServiceNameServiceSpec**](HostNatServiceNameServiceSpec.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_nat_service_spec import HostNatServiceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostNatServiceSpec from a JSON string
host_nat_service_spec_instance = HostNatServiceSpec.from_json(json)
# print the JSON string representation of the object
print HostNatServiceSpec.to_json()

# convert the object into a dict
host_nat_service_spec_dict = host_nat_service_spec_instance.to_dict()
# create an instance of HostNatServiceSpec from a dict
host_nat_service_spec_form_dict = host_nat_service_spec.from_dict(host_nat_service_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


