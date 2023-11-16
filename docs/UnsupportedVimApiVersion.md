# UnsupportedVimApiVersion

This exception will be thrown if a client tries to connect with a unsupported version of the Vim API.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 

## Example

```python
from vmware_vi.models.unsupported_vim_api_version import UnsupportedVimApiVersion

# TODO update the JSON string below
json = "{}"
# create an instance of UnsupportedVimApiVersion from a JSON string
unsupported_vim_api_version_instance = UnsupportedVimApiVersion.from_json(json)
# print the JSON string representation of the object
print UnsupportedVimApiVersion.to_json()

# convert the object into a dict
unsupported_vim_api_version_dict = unsupported_vim_api_version_instance.to_dict()
# create an instance of UnsupportedVimApiVersion from a dict
unsupported_vim_api_version_form_dict = unsupported_vim_api_version.from_dict(unsupported_vim_api_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


