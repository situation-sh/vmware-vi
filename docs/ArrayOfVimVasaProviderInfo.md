# ArrayOfVimVasaProviderInfo

A boxed array of *VimVasaProviderInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VimVasaProviderInfo]**](VimVasaProviderInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vim_vasa_provider_info import ArrayOfVimVasaProviderInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVimVasaProviderInfo from a JSON string
array_of_vim_vasa_provider_info_instance = ArrayOfVimVasaProviderInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfVimVasaProviderInfo.to_json()

# convert the object into a dict
array_of_vim_vasa_provider_info_dict = array_of_vim_vasa_provider_info_instance.to_dict()
# create an instance of ArrayOfVimVasaProviderInfo from a dict
array_of_vim_vasa_provider_info_form_dict = array_of_vim_vasa_provider_info.from_dict(array_of_vim_vasa_provider_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


