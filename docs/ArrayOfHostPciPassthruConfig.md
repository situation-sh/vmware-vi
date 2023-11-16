# ArrayOfHostPciPassthruConfig

A boxed array of *HostPciPassthruConfig*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPciPassthruConfig]**](HostPciPassthruConfig.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_pci_passthru_config import ArrayOfHostPciPassthruConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPciPassthruConfig from a JSON string
array_of_host_pci_passthru_config_instance = ArrayOfHostPciPassthruConfig.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPciPassthruConfig.to_json()

# convert the object into a dict
array_of_host_pci_passthru_config_dict = array_of_host_pci_passthru_config_instance.to_dict()
# create an instance of ArrayOfHostPciPassthruConfig from a dict
array_of_host_pci_passthru_config_form_dict = array_of_host_pci_passthru_config.from_dict(array_of_host_pci_passthru_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


