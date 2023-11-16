# WitnessNodeInfo

The WitnessNodeInfo class defines configuration information for the Witness node in the cluster  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_settings** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | 
**bios_uuid** | **str** | BIOS UUID for the node.  It is set only if the VCHA Cluster was formed using automatic provisioning by the deploy API.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.witness_node_info import WitnessNodeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of WitnessNodeInfo from a JSON string
witness_node_info_instance = WitnessNodeInfo.from_json(json)
# print the JSON string representation of the object
print WitnessNodeInfo.to_json()

# convert the object into a dict
witness_node_info_dict = witness_node_info_instance.to_dict()
# create an instance of WitnessNodeInfo from a dict
witness_node_info_form_dict = witness_node_info.from_dict(witness_node_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


