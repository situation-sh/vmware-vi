# OvfOptionInfo

Represents the OVF options the server support for import and export of OVFs  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**option** | **str** | The name of the OVF option that is supported by the server  ***Since:*** vSphere API 5.1  | 
**description** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.ovf_option_info import OvfOptionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OvfOptionInfo from a JSON string
ovf_option_info_instance = OvfOptionInfo.from_json(json)
# print the JSON string representation of the object
print OvfOptionInfo.to_json()

# convert the object into a dict
ovf_option_info_dict = ovf_option_info_instance.to_dict()
# create an instance of OvfOptionInfo from a dict
ovf_option_info_form_dict = ovf_option_info.from_dict(ovf_option_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


