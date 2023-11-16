# ArrayOfHostPciPassthruInfo

A boxed array of *HostPciPassthruInfo*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPciPassthruInfo]**](HostPciPassthruInfo.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_pci_passthru_info import ArrayOfHostPciPassthruInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPciPassthruInfo from a JSON string
array_of_host_pci_passthru_info_instance = ArrayOfHostPciPassthruInfo.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPciPassthruInfo.to_json()

# convert the object into a dict
array_of_host_pci_passthru_info_dict = array_of_host_pci_passthru_info_instance.to_dict()
# create an instance of ArrayOfHostPciPassthruInfo from a dict
array_of_host_pci_passthru_info_form_dict = array_of_host_pci_passthru_info.from_dict(array_of_host_pci_passthru_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


