# VmRequirementsExceedCurrentEVCModeEvent

The virtual machine is using features that exceed what the host is capable of providing.  This may occur when joining an EVC cluster while the virtual machine is powered on. The most common resolution is to power cycle the virtual machine.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_requirements_exceed_current_evc_mode_event import VmRequirementsExceedCurrentEVCModeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmRequirementsExceedCurrentEVCModeEvent from a JSON string
vm_requirements_exceed_current_evc_mode_event_instance = VmRequirementsExceedCurrentEVCModeEvent.from_json(json)
# print the JSON string representation of the object
print VmRequirementsExceedCurrentEVCModeEvent.to_json()

# convert the object into a dict
vm_requirements_exceed_current_evc_mode_event_dict = vm_requirements_exceed_current_evc_mode_event_instance.to_dict()
# create an instance of VmRequirementsExceedCurrentEVCModeEvent from a dict
vm_requirements_exceed_current_evc_mode_event_form_dict = vm_requirements_exceed_current_evc_mode_event.from_dict(vm_requirements_exceed_current_evc_mode_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


