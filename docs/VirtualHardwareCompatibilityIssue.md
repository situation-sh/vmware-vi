# VirtualHardwareCompatibilityIssue

There is a problem with the compatibility between the intended execution host and the virtual machine.  This may be an error or warning depending on the specific fault subclass. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.virtual_hardware_compatibility_issue import VirtualHardwareCompatibilityIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualHardwareCompatibilityIssue from a JSON string
virtual_hardware_compatibility_issue_instance = VirtualHardwareCompatibilityIssue.from_json(json)
# print the JSON string representation of the object
print VirtualHardwareCompatibilityIssue.to_json()

# convert the object into a dict
virtual_hardware_compatibility_issue_dict = virtual_hardware_compatibility_issue_instance.to_dict()
# create an instance of VirtualHardwareCompatibilityIssue from a dict
virtual_hardware_compatibility_issue_form_dict = virtual_hardware_compatibility_issue.from_dict(virtual_hardware_compatibility_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


