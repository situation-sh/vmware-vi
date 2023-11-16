# ArrayOfVirtualNicManagerNetConfig

A boxed array of *VirtualNicManagerNetConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualNicManagerNetConfig]**](VirtualNicManagerNetConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_nic_manager_net_config import ArrayOfVirtualNicManagerNetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualNicManagerNetConfig from a JSON string
array_of_virtual_nic_manager_net_config_instance = ArrayOfVirtualNicManagerNetConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualNicManagerNetConfig.to_json()

# convert the object into a dict
array_of_virtual_nic_manager_net_config_dict = array_of_virtual_nic_manager_net_config_instance.to_dict()
# create an instance of ArrayOfVirtualNicManagerNetConfig from a dict
array_of_virtual_nic_manager_net_config_form_dict = array_of_virtual_nic_manager_net_config.from_dict(array_of_virtual_nic_manager_net_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


