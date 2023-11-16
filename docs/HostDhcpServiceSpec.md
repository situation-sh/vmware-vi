# HostDhcpServiceSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_switch** | **str** | The name of the virtual switch to which DHCP service is connected.  ***Since:*** VI API 2.5  | 
**default_lease_duration** | **int** | The default DHCP lease duration (minutes).  ***Since:*** VI API 2.5  | 
**lease_begin_ip** | **str** | The start of the IP address range served by the DHCP service.  ***Since:*** VI API 2.5  | 
**lease_end_ip** | **str** | The end of the IP address range served by the DHCP service.  ***Since:*** VI API 2.5  | 
**max_lease_duration** | **int** | The maximum DHCP lease duration (minutes).  ***Since:*** VI API 2.5  | 
**unlimited_lease** | **bool** | A flag to indicate whether or not unlimited DHCP lease durations are allowed.  ***Since:*** VI API 2.5  | 
**ip_subnet_addr** | **str** | Subnet served by DHCP service.  ***Since:*** VI API 2.5  | 
**ip_subnet_mask** | **str** | Subnet mask of network served by DHCP service.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.host_dhcp_service_spec import HostDhcpServiceSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostDhcpServiceSpec from a JSON string
host_dhcp_service_spec_instance = HostDhcpServiceSpec.from_json(json)
# print the JSON string representation of the object
print HostDhcpServiceSpec.to_json()

# convert the object into a dict
host_dhcp_service_spec_dict = host_dhcp_service_spec_instance.to_dict()
# create an instance of HostDhcpServiceSpec from a dict
host_dhcp_service_spec_form_dict = host_dhcp_service_spec.from_dict(host_dhcp_service_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


