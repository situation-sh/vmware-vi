# HostPciPassthruInfo

This data object provides information about the state of PciPassthru for all pci devices.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The name ID of this PCI, composed of \&quot;bus:slot.function\&quot;.  ***Since:*** vSphere API 4.0  | 
**dependent_device** | **str** | Device which needs to be unclaimed by vmkernel (may be bridge)  ***Since:*** vSphere API 4.0  | 
**passthru_enabled** | **bool** | Whether passThru has been configured by the user  ***Since:*** vSphere API 4.0  | 
**passthru_capable** | **bool** | Whether passThru is even possible for this device (decided by vmkctl)  ***Since:*** vSphere API 4.0  | 
**passthru_active** | **bool** | Whether passThru is active for this device (meaning enabled + rebooted)  ***Since:*** vSphere API 4.0  | 
**hardware_label** | **str** | The hardware label of this PCI device.  ***Since:*** vSphere API 7.0.2.0  | [optional] 

## Example

```python
from vmware_vi.models.host_pci_passthru_info import HostPciPassthruInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostPciPassthruInfo from a JSON string
host_pci_passthru_info_instance = HostPciPassthruInfo.from_json(json)
# print the JSON string representation of the object
print HostPciPassthruInfo.to_json()

# convert the object into a dict
host_pci_passthru_info_dict = host_pci_passthru_info_instance.to_dict()
# create an instance of HostPciPassthruInfo from a dict
host_pci_passthru_info_form_dict = host_pci_passthru_info.from_dict(host_pci_passthru_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


