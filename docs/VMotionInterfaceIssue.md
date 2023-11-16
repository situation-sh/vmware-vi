# VMotionInterfaceIssue

A VMotion interface has a problem.  This may be an error or warning depending on the specific fault subclass. This is an error or warning only when migrating a powered-on virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at_source_host** | **bool** | Whether this error is for the source host.  | 
**failed_host** | **str** | The name of the host with the bad interface.  | 
**failed_host_entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.v_motion_interface_issue import VMotionInterfaceIssue

# TODO update the JSON string below
json = "{}"
# create an instance of VMotionInterfaceIssue from a JSON string
v_motion_interface_issue_instance = VMotionInterfaceIssue.from_json(json)
# print the JSON string representation of the object
print VMotionInterfaceIssue.to_json()

# convert the object into a dict
v_motion_interface_issue_dict = v_motion_interface_issue_instance.to_dict()
# create an instance of VMotionInterfaceIssue from a dict
v_motion_interface_issue_form_dict = v_motion_interface_issue.from_dict(v_motion_interface_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


