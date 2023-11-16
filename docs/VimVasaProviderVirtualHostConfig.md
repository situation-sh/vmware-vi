# VimVasaProviderVirtualHostConfig

Holds VirtualHost configuration information when VASA 5.0 or greater VVOL VASA Provider supports MultiVC through VirtualHosts. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vhost_name** | **str** | Virtual Host FQDN on VASA Provider.  If set, it&#39;s used as SNI hostname in outgoing VASA Provider connection.  | [optional] 
**service_host** | **str** | IP address where Virtual Host is running  | 
**service_port** | **int** | Dedicated port for the virtual host.  If not specified, default VirtualHost port is used to communicate with VASA Provider.  | [optional] 

## Example

```python
from vmware_vi.models.vim_vasa_provider_virtual_host_config import VimVasaProviderVirtualHostConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VimVasaProviderVirtualHostConfig from a JSON string
vim_vasa_provider_virtual_host_config_instance = VimVasaProviderVirtualHostConfig.from_json(json)
# print the JSON string representation of the object
print VimVasaProviderVirtualHostConfig.to_json()

# convert the object into a dict
vim_vasa_provider_virtual_host_config_dict = vim_vasa_provider_virtual_host_config_instance.to_dict()
# create an instance of VimVasaProviderVirtualHostConfig from a dict
vim_vasa_provider_virtual_host_config_form_dict = vim_vasa_provider_virtual_host_config.from_dict(vim_vasa_provider_virtual_host_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


