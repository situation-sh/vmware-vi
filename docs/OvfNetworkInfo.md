# OvfNetworkInfo

The name and description of a network as specified by the OVF descriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from vmware_vi.models.ovf_network_info import OvfNetworkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OvfNetworkInfo from a JSON string
ovf_network_info_instance = OvfNetworkInfo.from_json(json)
# print the JSON string representation of the object
print OvfNetworkInfo.to_json()

# convert the object into a dict
ovf_network_info_dict = ovf_network_info_instance.to_dict()
# create an instance of OvfNetworkInfo from a dict
ovf_network_info_form_dict = ovf_network_info.from_dict(ovf_network_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


