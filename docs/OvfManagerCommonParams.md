# OvfManagerCommonParams

A common super-class for basic OVF descriptor parameters  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | The locale-identifier to choose from the descriptor.  If empty, the default locale on the server is used.  ***Since:*** vSphere API 4.0  | 
**deployment_option** | **str** | The key of the chosen deployment option.  If empty, the default option is chosen. The list of possible deployment options is returned in the result of parseDescriptor.  ***Since:*** vSphere API 4.0  | 
**msg_bundle** | [**List[KeyValue]**](KeyValue.md) | An optional set of localization strings to be used.  The server will use these message strings to localize information in the result and in error and warning messages.  This argument allows a client to pass messages from external string bundles. The client is responsible for selecting the right string bundle (based on locale) and parsing the external string bundle. The passed in key/value pairs are looked up before any messages included in the OVF descriptor itself.  ***Since:*** vSphere API 4.0  | [optional] 
**import_option** | **List[str]** | An optional argument for modifing the OVF parsing.  When the server parses an OVF descriptor a set of options can be used to modify the parsing. The argument is a list of keywords.  To get a list of supported keywords see *OvfManager.ovfImportOption*. Unknown options will be ignored by the server.  ***Since:*** vSphere API 5.1  | [optional] 

## Example

```python
from vmware_vi.models.ovf_manager_common_params import OvfManagerCommonParams

# TODO update the JSON string below
json = "{}"
# create an instance of OvfManagerCommonParams from a JSON string
ovf_manager_common_params_instance = OvfManagerCommonParams.from_json(json)
# print the JSON string representation of the object
print OvfManagerCommonParams.to_json()

# convert the object into a dict
ovf_manager_common_params_dict = ovf_manager_common_params_instance.to_dict()
# create an instance of OvfManagerCommonParams from a dict
ovf_manager_common_params_form_dict = ovf_manager_common_params.from_dict(ovf_manager_common_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


