# OvfNetworkMapping

A NetworkMapping is a choice made by the caller about which VI network to use for a specific network in the OVF descriptor.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**network** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.ovf_network_mapping import OvfNetworkMapping

# TODO update the JSON string below
json = "{}"
# create an instance of OvfNetworkMapping from a JSON string
ovf_network_mapping_instance = OvfNetworkMapping.from_json(json)
# print the JSON string representation of the object
print OvfNetworkMapping.to_json()

# convert the object into a dict
ovf_network_mapping_dict = ovf_network_mapping_instance.to_dict()
# create an instance of OvfNetworkMapping from a dict
ovf_network_mapping_form_dict = ovf_network_mapping.from_dict(ovf_network_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


