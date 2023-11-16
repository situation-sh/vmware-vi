# HostDhcpService

A dynamic host control protocol (DHCP) service instance serves IP addresses to a single virtual network subnet.  The instances may be handled collectively by a single server. This decision can be made during implementation.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The instance ID of the DHCP service.  ***Since:*** VI API 2.5  | 
**spec** | [**HostDhcpServiceSpec**](HostDhcpServiceSpec.md) |  | 

## Example

```python
from vmware_vi.models.host_dhcp_service import HostDhcpService

# TODO update the JSON string below
json = "{}"
# create an instance of HostDhcpService from a JSON string
host_dhcp_service_instance = HostDhcpService.from_json(json)
# print the JSON string representation of the object
print HostDhcpService.to_json()

# convert the object into a dict
host_dhcp_service_dict = host_dhcp_service_instance.to_dict()
# create an instance of HostDhcpService from a dict
host_dhcp_service_form_dict = host_dhcp_service.from_dict(host_dhcp_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


