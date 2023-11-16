# HostIpConfig

The IP configuration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp** | **bool** | The flag to indicate whether or not DHCP (dynamic host control protocol) is enabled.  If this property is set to true, the ipAddress and the subnetMask strings cannot be set explicitly.  | 
**ip_address** | **str** | The IP address currently used by the network adapter.  All IP addresses are specified using IPv4 dot notation. For example, \&quot;192.168.0.1\&quot;. Subnet addresses and netmasks are specified using the same notation.  **Note**: When DHCP is enabled, this property reflects the current IP configuration and cannot be set. When DHCP is not enabled, this property can be set explicitly.  | [optional] 
**subnet_mask** | **str** | The subnet mask.  **Note**: When DHCP is not enabled, this property can be set explicitly. When DHCP is enabled, this property reflects the current IP configuration and cannot be set.  | [optional] 
**ip_v6_config** | [**HostIpConfigIpV6AddressConfiguration**](HostIpConfigIpV6AddressConfiguration.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_ip_config import HostIpConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostIpConfig from a JSON string
host_ip_config_instance = HostIpConfig.from_json(json)
# print the JSON string representation of the object
print HostIpConfig.to_json()

# convert the object into a dict
host_ip_config_dict = host_ip_config_instance.to_dict()
# create an instance of HostIpConfig from a dict
host_ip_config_form_dict = host_ip_config.from_dict(host_ip_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


