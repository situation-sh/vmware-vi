# ArrayOfVimVasaProvider

A boxed array of *VimVasaProvider*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VimVasaProvider]**](VimVasaProvider.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vim_vasa_provider import ArrayOfVimVasaProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVimVasaProvider from a JSON string
array_of_vim_vasa_provider_instance = ArrayOfVimVasaProvider.from_json(json)
# print the JSON string representation of the object
print ArrayOfVimVasaProvider.to_json()

# convert the object into a dict
array_of_vim_vasa_provider_dict = array_of_vim_vasa_provider_instance.to_dict()
# create an instance of ArrayOfVimVasaProvider from a dict
array_of_vim_vasa_provider_form_dict = array_of_vim_vasa_provider.from_dict(array_of_vim_vasa_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


