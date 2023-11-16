# ArrayOfVirtualHardwareCompatibilityIssue

A boxed array of *VirtualHardwareCompatibilityIssue*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualHardwareCompatibilityIssue]**](VirtualHardwareCompatibilityIssue.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_hardware_compatibility_issue import ArrayOfVirtualHardwareCompatibilityIssue

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualHardwareCompatibilityIssue from a JSON string
array_of_virtual_hardware_compatibility_issue_instance = ArrayOfVirtualHardwareCompatibilityIssue.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualHardwareCompatibilityIssue.to_json()

# convert the object into a dict
array_of_virtual_hardware_compatibility_issue_dict = array_of_virtual_hardware_compatibility_issue_instance.to_dict()
# create an instance of ArrayOfVirtualHardwareCompatibilityIssue from a dict
array_of_virtual_hardware_compatibility_issue_form_dict = array_of_virtual_hardware_compatibility_issue.from_dict(array_of_virtual_hardware_compatibility_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


