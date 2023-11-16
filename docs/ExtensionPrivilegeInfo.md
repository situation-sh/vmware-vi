# ExtensionPrivilegeInfo

This data object type describes privileges defined by the extension.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priv_id** | **str** | The ID of the privilege.  The format should be &amp;quot;&amp;lt;group name&amp;gt;.&amp;lt;privilege name&amp;gt;&amp;quot;. The group name should be the same as the privGroupName property.  The privilege name should follow java package naming conventions for uniqueness. The set of characters allowed follow the same rules as *Extension.key*.  ***Since:*** VI API 2.5  | 
**priv_group_name** | **str** | Hierarchical group name.  Each level of the grouping hierarchy is separated by a \&quot;.\&quot; so group names may not include a \&quot;.\&quot;. *AuthorizationPrivilege.privGroupName*.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.extension_privilege_info import ExtensionPrivilegeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionPrivilegeInfo from a JSON string
extension_privilege_info_instance = ExtensionPrivilegeInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionPrivilegeInfo.to_json()

# convert the object into a dict
extension_privilege_info_dict = extension_privilege_info_instance.to_dict()
# create an instance of ExtensionPrivilegeInfo from a dict
extension_privilege_info_form_dict = extension_privilege_info.from_dict(extension_privilege_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


