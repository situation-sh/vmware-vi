# OvfPropertyNetworkExport

VIM property type that refers to a network that does not exist in the package since no virtual machines are hooked up to it.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network** | **str** | name of network  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.ovf_property_network_export import OvfPropertyNetworkExport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfPropertyNetworkExport from a JSON string
ovf_property_network_export_instance = OvfPropertyNetworkExport.from_json(json)
# print the JSON string representation of the object
print OvfPropertyNetworkExport.to_json()

# convert the object into a dict
ovf_property_network_export_dict = ovf_property_network_export_instance.to_dict()
# create an instance of OvfPropertyNetworkExport from a dict
ovf_property_network_export_form_dict = ovf_property_network_export.from_dict(ovf_property_network_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


