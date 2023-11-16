# ExtManagedEntityInfo

This data object contains information about entities managed by this extension.  The data can be used by clients to show extra information about managed virtual machines or vApps, such as a custom icon and a description of the entity.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Managed entity type, as defined by the extension.  This matches the *type* field in the configuration about a virtual machine or vApp.  ***Since:*** vSphere API 5.0  | 
**small_icon_url** | **str** | The URL to a 16x16 pixel icon in PNG format for entities of this type managed by this extension.  The design of the icon should allow for the possibility of it being badged with the power state of the entity by the vSphere client. If you do not provide this icon, the icon at *iconUrl*, if found, is scaled down to 16x16 pixels.  ***Since:*** vSphere API 5.0  | [optional] 
**icon_url** | **str** | The URL to an icon in PNG format that is no larger than 256x256 pixels.  This icon will be scaled to 16x16, 32x32, 64x64, and 128x128 if needed. The icon is shown for all entities of this type managed by this extension.  ***Since:*** vSphere API 5.1  | [optional] 
**description** | **str** | Description of this managed entity type.  This is typically displayed by clients, and should provide users with information about the function of entities of this type.  ***Since:*** vSphere API 5.0  | [optional] 

## Example

```python
from vmware_vi.models.ext_managed_entity_info import ExtManagedEntityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtManagedEntityInfo from a JSON string
ext_managed_entity_info_instance = ExtManagedEntityInfo.from_json(json)
# print the JSON string representation of the object
print ExtManagedEntityInfo.to_json()

# convert the object into a dict
ext_managed_entity_info_dict = ext_managed_entity_info_instance.to_dict()
# create an instance of ExtManagedEntityInfo from a dict
ext_managed_entity_info_form_dict = ext_managed_entity_info.from_dict(ext_managed_entity_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


