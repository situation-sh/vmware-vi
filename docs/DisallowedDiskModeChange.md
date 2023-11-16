# DisallowedDiskModeChange

Thrown when the *VirtualMachine.ReconfigVM_Task* operation includes a change to the *VirtualDiskMode_enum* property.  This property cannot be changed as long as a virtual machine has an existing snapshot. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.disallowed_disk_mode_change import DisallowedDiskModeChange

# TODO update the JSON string below
json = "{}"
# create an instance of DisallowedDiskModeChange from a JSON string
disallowed_disk_mode_change_instance = DisallowedDiskModeChange.from_json(json)
# print the JSON string representation of the object
print DisallowedDiskModeChange.to_json()

# convert the object into a dict
disallowed_disk_mode_change_dict = disallowed_disk_mode_change_instance.to_dict()
# create an instance of DisallowedDiskModeChange from a dict
disallowed_disk_mode_change_form_dict = disallowed_disk_mode_change.from_dict(disallowed_disk_mode_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


