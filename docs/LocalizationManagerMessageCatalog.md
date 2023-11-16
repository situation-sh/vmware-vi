# LocalizationManagerMessageCatalog

Description of an available message catalog  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_name** | **str** | The module or extension that publishes this catalog.  The moduleName will be empty for the core catalogs for the VirtualCenter server itself.  ***Since:*** vSphere API 4.0  | 
**catalog_name** | **str** | The name of the catalog.  ***Since:*** vSphere API 4.0  | 
**locale** | **str** | The locale for the catalog.  ***Since:*** vSphere API 4.0  | 
**catalog_uri** | **str** | The URI (relative to the connection URL for the VirtualCenter server itself) from which the catalog can be downloaded.  The caller will need to augment this with a scheme and authority (host and port) to make a complete URL.  ***Since:*** vSphere API 4.0  | 
**last_modified** | **datetime** | The last-modified time of the catalog file, if available  ***Since:*** vSphere API 4.0  | [optional] 
**md5sum** | **str** | The checksum of the catalog file, if available  ***Since:*** vSphere API 4.0  | [optional] 
**version** | **str** | The version of the catalog file, if available The format is dot-separated version string, e.g.  \&quot;1.2.3\&quot;.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.localization_manager_message_catalog import LocalizationManagerMessageCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of LocalizationManagerMessageCatalog from a JSON string
localization_manager_message_catalog_instance = LocalizationManagerMessageCatalog.from_json(json)
# print the JSON string representation of the object
print LocalizationManagerMessageCatalog.to_json()

# convert the object into a dict
localization_manager_message_catalog_dict = localization_manager_message_catalog_instance.to_dict()
# create an instance of LocalizationManagerMessageCatalog from a dict
localization_manager_message_catalog_form_dict = localization_manager_message_catalog.from_dict(localization_manager_message_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


