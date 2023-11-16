# ExtensionFaultTypeInfo

This data object type describes fault types defined by the extension.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fault_id** | **str** | The ID of the fault type.  Should follow java package naming conventions for uniqueness.  ***Since:*** VI API 2.5  | 

## Example

```python
from vmware_vi.models.extension_fault_type_info import ExtensionFaultTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionFaultTypeInfo from a JSON string
extension_fault_type_info_instance = ExtensionFaultTypeInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionFaultTypeInfo.to_json()

# convert the object into a dict
extension_fault_type_info_dict = extension_fault_type_info_instance.to_dict()
# create an instance of ExtensionFaultTypeInfo from a dict
extension_fault_type_info_form_dict = extension_fault_type_info.from_dict(extension_fault_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


