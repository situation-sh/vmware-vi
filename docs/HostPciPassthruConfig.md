# HostPciPassthruConfig

This data object provides information about the state of PciPassthru for all pci devices.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name ID of this PCI, composed of \&quot;bus:slot.function\&quot;.  ***Since:*** vSphere API 4.0  | 
**passthru_enabled** | **bool** | Whether passThru has been configured for this device  ***Since:*** vSphere API 4.0  | 
**apply_now** | **bool** | Whether the passThru config should take effect without rebooting ESX.  When unset, the behavior will be determined automatically based on *HostCapability.deviceRebindWithoutRebootSupported*. If the configuration can be applied immediately, it will be, otherwise the changes will take effect after reboot.  ***Since:*** vSphere API 7.0  | [optional] 
**hardware_label** | **str** | The hardware label of the this PCI device.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.host_pci_passthru_config import HostPciPassthruConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostPciPassthruConfig from a JSON string
host_pci_passthru_config_instance = HostPciPassthruConfig.from_json(json)
# print the JSON string representation of the object
print HostPciPassthruConfig.to_json()

# convert the object into a dict
host_pci_passthru_config_dict = host_pci_passthru_config_instance.to_dict()
# create an instance of HostPciPassthruConfig from a dict
host_pci_passthru_config_form_dict = host_pci_passthru_config.from_dict(host_pci_passthru_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


