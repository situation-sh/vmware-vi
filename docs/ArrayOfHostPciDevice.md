# ArrayOfHostPciDevice

A boxed array of *HostPciDevice*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostPciDevice]**](HostPciDevice.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_pci_device import ArrayOfHostPciDevice

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostPciDevice from a JSON string
array_of_host_pci_device_instance = ArrayOfHostPciDevice.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostPciDevice.to_json()

# convert the object into a dict
array_of_host_pci_device_dict = array_of_host_pci_device_instance.to_dict()
# create an instance of ArrayOfHostPciDevice from a dict
array_of_host_pci_device_form_dict = array_of_host_pci_device.from_dict(array_of_host_pci_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


