# VimVasaProvider

Data object representing VASA Provider.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Provider UID.  This is populated with namespace prefixed to providerId, which uniquely identifies a VASA Provider. Both namespace and providerId are sourced from Vasa Provider and available within SMS. This field helps in preventing a regeneration of duplicate VASA Provider within vvold when a user attempts to register the same VP using different names or alternative urls.  ***Since:*** vSphere API 6.7  | [optional] 
**url** | **str** | VASA Provider URL.  In VirtualHost based MultiVC setup, this is set to default virtual host&#39;s URL.  ***Since:*** vSphere API 6.0  | 
**name** | **str** | Name  ***Since:*** vSphere API 6.0  | [optional] 
**self_signed_certificate** | **str** | Self-signed certificate of VASA provider.  In VirtualHost based MultiVC setup, this is set to default virtual host&#39;s self-signed certificate.  ***Since:*** vSphere API 6.0  | [optional] 
**vhost_config** | [**VimVasaProviderVirtualHostConfig**](VimVasaProviderVirtualHostConfig.md) |  | [optional] 
**version_id** | **int** | SMS supported VASA provider versionId.  i-e if versionX corresponds to VASA version supported by SMS, then X needs to be set here. versionX corresponds to SMS supported VASA versions are, 1.0-&amp;gt;version1, 1.5-&amp;gt;version2, 2.0-&amp;gt;version3, 3.0-&amp;gt;version4, 3.5-&amp;gt;version5, 4.0-&amp;gt;version6, 5.0-&amp;gt;version7, etc. For example: If SMS is connecting to VASA 5.0, the this field should be set to 7.  | [optional] 

## Example

```python
from vmware_vi.models.vim_vasa_provider import VimVasaProvider

# TODO update the JSON string below
json = "{}"
# create an instance of VimVasaProvider from a JSON string
vim_vasa_provider_instance = VimVasaProvider.from_json(json)
# print the JSON string representation of the object
print VimVasaProvider.to_json()

# convert the object into a dict
vim_vasa_provider_dict = vim_vasa_provider_instance.to_dict()
# create an instance of VimVasaProvider from a dict
vim_vasa_provider_form_dict = vim_vasa_provider.from_dict(vim_vasa_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


