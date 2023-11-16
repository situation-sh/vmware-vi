# HostDnsConfigSpec

Dataobject for configuring the DNS settings on the host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**virtual_nic_connection** | [**HostVirtualNicConnection**](HostVirtualNicConnection.md) |  | [optional] 
**virtual_nic_connection_v6** | [**HostVirtualNicConnection**](HostVirtualNicConnection.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_dns_config_spec import HostDnsConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostDnsConfigSpec from a JSON string
host_dns_config_spec_instance = HostDnsConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostDnsConfigSpec.to_json()

# convert the object into a dict
host_dns_config_spec_dict = host_dns_config_spec_instance.to_dict()
# create an instance of HostDnsConfigSpec from a dict
host_dns_config_spec_form_dict = host_dns_config_spec.from_dict(host_dns_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


