# VimVasaProviderStatePerArray

Per Storage Array VP status.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **int** | Priority of the provider for the given array  ***Since:*** vSphere API 6.0  | 
**array_id** | **str** | Storage Array object Id  ***Since:*** vSphere API 6.0  | 
**active** | **bool** | Indicates whether a VASA Provider (*VimVasaProvider.url*) is active for the specified storage array.  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.vim_vasa_provider_state_per_array import VimVasaProviderStatePerArray

# TODO update the JSON string below
json = "{}"
# create an instance of VimVasaProviderStatePerArray from a JSON string
vim_vasa_provider_state_per_array_instance = VimVasaProviderStatePerArray.from_json(json)
# print the JSON string representation of the object
print VimVasaProviderStatePerArray.to_json()

# convert the object into a dict
vim_vasa_provider_state_per_array_dict = vim_vasa_provider_state_per_array_instance.to_dict()
# create an instance of VimVasaProviderStatePerArray from a dict
vim_vasa_provider_state_per_array_form_dict = vim_vasa_provider_state_per_array.from_dict(vim_vasa_provider_state_per_array_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


