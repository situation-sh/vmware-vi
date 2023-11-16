# CustomizationAdapterMapping

Data object type to associate a virtual network adapter with its IP settings. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mac_address** | **str** | The MAC address of a network adapter being customized.  The client cannot change this value because the guest operating system has no control over the MAC address of a virtual network adapter.  This property is optional. If it is not included, the customization process maps the settings from the list of AdapterMappings.IPSettings in the Specification.nicSettingMap to the virtual machine&#39;s network adapters, in PCI slot order. The first virtual network adapter on the PCI bus is assigned nicSettingMap\\[0\\].IPSettings, the second adapter is assigned nicSettingMap\\[1\\].IPSettings, and so on.  In vSphere 7.0 series, the MAC addresses must be specified in the ascending order of pciSlotNumber, otherwise a MAC address mismatch error will be reported. For further details, see the https://kb.vmware.com/s/article/87648  | [optional] 
**adapter** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | 

## Example

```python
from vmware_vi.models.customization_adapter_mapping import CustomizationAdapterMapping

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationAdapterMapping from a JSON string
customization_adapter_mapping_instance = CustomizationAdapterMapping.from_json(json)
# print the JSON string representation of the object
print CustomizationAdapterMapping.to_json()

# convert the object into a dict
customization_adapter_mapping_dict = customization_adapter_mapping_instance.to_dict()
# create an instance of CustomizationAdapterMapping from a dict
customization_adapter_mapping_form_dict = customization_adapter_mapping.from_dict(customization_adapter_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


