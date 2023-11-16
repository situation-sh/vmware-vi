# LegacyNetworkInterfaceInUse

A virtual machine's network connectivity cannot be determined because it uses a legacy network interface.  If returned as part of migration checks, this is an error if the virtual machine is currently connected to the legacy interface, and a warning otherwise. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.legacy_network_interface_in_use import LegacyNetworkInterfaceInUse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyNetworkInterfaceInUse from a JSON string
legacy_network_interface_in_use_instance = LegacyNetworkInterfaceInUse.from_json(json)
# print the JSON string representation of the object
print LegacyNetworkInterfaceInUse.to_json()

# convert the object into a dict
legacy_network_interface_in_use_dict = legacy_network_interface_in_use_instance.to_dict()
# create an instance of LegacyNetworkInterfaceInUse from a dict
legacy_network_interface_in_use_form_dict = legacy_network_interface_in_use.from_dict(legacy_network_interface_in_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


