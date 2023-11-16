# ArrayOfExtensionClientInfo

A boxed array of *ExtensionClientInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtensionClientInfo]**](ExtensionClientInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extension_client_info import ArrayOfExtensionClientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtensionClientInfo from a JSON string
array_of_extension_client_info_instance = ArrayOfExtensionClientInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtensionClientInfo.to_json()

# convert the object into a dict
array_of_extension_client_info_dict = array_of_extension_client_info_instance.to_dict()
# create an instance of ArrayOfExtensionClientInfo from a dict
array_of_extension_client_info_form_dict = array_of_extension_client_info.from_dict(array_of_extension_client_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


