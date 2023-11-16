# ArrayOfExtensionPrivilegeInfo

A boxed array of *ExtensionPrivilegeInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[ExtensionPrivilegeInfo]**](ExtensionPrivilegeInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_extension_privilege_info import ArrayOfExtensionPrivilegeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfExtensionPrivilegeInfo from a JSON string
array_of_extension_privilege_info_instance = ArrayOfExtensionPrivilegeInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfExtensionPrivilegeInfo.to_json()

# convert the object into a dict
array_of_extension_privilege_info_dict = array_of_extension_privilege_info_instance.to_dict()
# create an instance of ArrayOfExtensionPrivilegeInfo from a dict
array_of_extension_privilege_info_form_dict = array_of_extension_privilege_info.from_dict(array_of_extension_privilege_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


