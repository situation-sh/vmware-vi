# VimVasaProviderInfo

Data object representing VASA Provider information.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**VimVasaProvider**](VimVasaProvider.md) |  | 
**array_state** | [**List[VimVasaProviderStatePerArray]**](VimVasaProviderStatePerArray.md) | Per-array State  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.vim_vasa_provider_info import VimVasaProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VimVasaProviderInfo from a JSON string
vim_vasa_provider_info_instance = VimVasaProviderInfo.from_json(json)
# print the JSON string representation of the object
print VimVasaProviderInfo.to_json()

# convert the object into a dict
vim_vasa_provider_info_dict = vim_vasa_provider_info_instance.to_dict()
# create an instance of VimVasaProviderInfo from a dict
vim_vasa_provider_info_form_dict = vim_vasa_provider_info.from_dict(vim_vasa_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


