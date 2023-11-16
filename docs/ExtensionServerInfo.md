# ExtensionServerInfo

This data object type describes a server for the extension.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Server url.  ***Since:*** VI API 2.5  | 
**description** | [**Description**](Description.md) |  | 
**company** | **str** | Company information.  ***Since:*** VI API 2.5  | 
**type** | **str** | Type of server (examples may include SOAP, REST, HTTP, etc.).  ***Since:*** VI API 2.5  | 
**admin_email** | **List[str]** | Extension administrator email addresses.  ***Since:*** VI API 2.5  | 
**server_thumbprint** | **str** | Thumbprint of the extension server certificate presented to clients  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.extension_server_info import ExtensionServerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionServerInfo from a JSON string
extension_server_info_instance = ExtensionServerInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionServerInfo.to_json()

# convert the object into a dict
extension_server_info_dict = extension_server_info_instance.to_dict()
# create an instance of ExtensionServerInfo from a dict
extension_server_info_form_dict = extension_server_info.from_dict(extension_server_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


