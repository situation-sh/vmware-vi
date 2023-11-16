# VmDasBeingResetWithScreenshotEvent

This event records when a virtual machine is reset by HA VM Health Monitoring on hosts that support the create screenshot api  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**screenshot_file_path** | **str** | The datastore path of the screenshot taken before resetting.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_das_being_reset_with_screenshot_event import VmDasBeingResetWithScreenshotEvent

# TODO update the JSON string below
json = "{}"
# create an instance of VmDasBeingResetWithScreenshotEvent from a JSON string
vm_das_being_reset_with_screenshot_event_instance = VmDasBeingResetWithScreenshotEvent.from_json(json)
# print the JSON string representation of the object
print VmDasBeingResetWithScreenshotEvent.to_json()

# convert the object into a dict
vm_das_being_reset_with_screenshot_event_dict = vm_das_being_reset_with_screenshot_event_instance.to_dict()
# create an instance of VmDasBeingResetWithScreenshotEvent from a dict
vm_das_being_reset_with_screenshot_event_form_dict = vm_das_being_reset_with_screenshot_event.from_dict(vm_das_being_reset_with_screenshot_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


