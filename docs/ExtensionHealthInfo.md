# ExtensionHealthInfo

This data object encapsulates the health specification for the extension.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | 

## Example

```python
from vmware_vi.models.extension_health_info import ExtensionHealthInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ExtensionHealthInfo from a JSON string
extension_health_info_instance = ExtensionHealthInfo.from_json(json)
# print the JSON string representation of the object
print ExtensionHealthInfo.to_json()

# convert the object into a dict
extension_health_info_dict = extension_health_info_instance.to_dict()
# create an instance of ExtensionHealthInfo from a dict
extension_health_info_form_dict = extension_health_info.from_dict(extension_health_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


