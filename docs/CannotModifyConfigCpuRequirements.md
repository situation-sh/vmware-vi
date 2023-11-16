# CannotModifyConfigCpuRequirements

A virtual machine's total CPU feature requirements are determined by overlaying the requirements specified in its configuration (if any) on top of the requirements specified in the descriptor for its guest OS.  It is therefore possible for a host change to implicitly change a virtual machine's CPU feature requirements. The guest OS descriptor may have different requirements on the new host. Or, if the virtual machine currently specifies requirements in its configuration, those requirements will be lost if the new host does not support this.  This fault indicates that the virtual machine's CPU feature requirements would change because of a migration, and also that the destination host does not support storing CPU feature requirements in the virtual machine's configuration. (If the destination host does support such an action, WillModifyConfigCpuRequirements is used instead of this fault.)  For a powered-off virtual machine, this is a warning. The migration may proceed, but the virtual machine will be operating under different CPU feature requirements if it is powered on after the migration.  For a powered-on or suspended virtual machine, this is an error. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.cannot_modify_config_cpu_requirements import CannotModifyConfigCpuRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of CannotModifyConfigCpuRequirements from a JSON string
cannot_modify_config_cpu_requirements_instance = CannotModifyConfigCpuRequirements.from_json(json)
# print the JSON string representation of the object
print CannotModifyConfigCpuRequirements.to_json()

# convert the object into a dict
cannot_modify_config_cpu_requirements_dict = cannot_modify_config_cpu_requirements_instance.to_dict()
# create an instance of CannotModifyConfigCpuRequirements from a dict
cannot_modify_config_cpu_requirements_form_dict = cannot_modify_config_cpu_requirements.from_dict(cannot_modify_config_cpu_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


