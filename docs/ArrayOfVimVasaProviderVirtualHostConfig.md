# ArrayOfVimVasaProviderVirtualHostConfig

A boxed array of *VimVasaProviderVirtualHostConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VimVasaProviderVirtualHostConfig]**](VimVasaProviderVirtualHostConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vim_vasa_provider_virtual_host_config import ArrayOfVimVasaProviderVirtualHostConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVimVasaProviderVirtualHostConfig from a JSON string
array_of_vim_vasa_provider_virtual_host_config_instance = ArrayOfVimVasaProviderVirtualHostConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfVimVasaProviderVirtualHostConfig.to_json()

# convert the object into a dict
array_of_vim_vasa_provider_virtual_host_config_dict = array_of_vim_vasa_provider_virtual_host_config_instance.to_dict()
# create an instance of ArrayOfVimVasaProviderVirtualHostConfig from a dict
array_of_vim_vasa_provider_virtual_host_config_form_dict = array_of_vim_vasa_provider_virtual_host_config.from_dict(array_of_vim_vasa_provider_virtual_host_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


