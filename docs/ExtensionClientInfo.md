# ExtensionClientInfo

This data object type describes a client of the extension.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Client version number as a dot-separated string.  For example, \&quot;1.0.0\&quot;  ***Since:*** VI API 2.5  | 
**description** | [**Description**](Description.md) |  | 
**company** | **str** | Company information.  ***Since:*** VI API 2.5  | 
**type** | **str** | Type of client (examples may include win32, .net, linux, etc.).  ***Since:*** VI API 2.5  | 
**url** | **str** | Plugin url.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.extension_client_info import ExtensionClientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionClientInfo from a JSON string
extension_client_info_instance = ExtensionClientInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionClientInfo.to_json()

# convert the object into a dict
extension_client_info_dict = extension_client_info_instance.to_dict()
# create an instance of ExtensionClientInfo from a dict
extension_client_info_form_dict = extension_client_info.from_dict(extension_client_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


