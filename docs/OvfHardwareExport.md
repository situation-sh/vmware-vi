# OvfHardwareExport

A common base class to host all the OvfLib Export Exceptions for hardware.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | [**VirtualDevice**](VirtualDevice.md) |  | [optional] 
**vm_path** | **str** | The path to the VM containing the device.  This path shows the location of the VM in the vApp hierarchy, on the form:  /ParentVApp/ChildVApp/VMName  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_hardware_export import OvfHardwareExport

# TODO update the JSON string below
json = "{}"
# create an instance of OvfHardwareExport from a JSON string
ovf_hardware_export_instance = OvfHardwareExport.from_json(json)
# print the JSON string representation of the object
print OvfHardwareExport.to_json()

# convert the object into a dict
ovf_hardware_export_dict = ovf_hardware_export_instance.to_dict()
# create an instance of OvfHardwareExport from a dict
ovf_hardware_export_form_dict = ovf_hardware_export.from_dict(ovf_hardware_export_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


