# WillModifyConfigCpuRequirements

A virtual machine's total CPU feature requirements are determined by overlaying the requirements specified in its configuration (if any) on top of the requirements specified in the descriptor for its guest OS.  It is therefore possible for a host change to implicitly change a virtual machine's CPU feature requirements. The guest OS descriptor may have different requirements on the new host. Or, if the virtual machine currently specifies requirements in its configuration, those requirements will be lost if the new host does not support this.  This fault indicates that the virtual machine's CPU feature requirements would change because of a migration, and also that the destination host does support storing CPU feature requirements in the virtual machine's configuration. (If the destination host does not support such an action, *CannotModifyConfigCpuRequirements* is used instead of this fault.)  This is a warning to notify the user that the migration process will adjust the virtual machine's configuration so that it will be operating under an unchanged set of CPU feature requirements on its new host. If the user wishes to expose the different guest OS requirements of the new host, the user will need to edit the virtual machine's configuration after the migration. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.will_modify_config_cpu_requirements import WillModifyConfigCpuRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of WillModifyConfigCpuRequirements from a JSON string
will_modify_config_cpu_requirements_instance = WillModifyConfigCpuRequirements.from_json(json)
# print the JSON string representation of the object
print WillModifyConfigCpuRequirements.to_json()

# convert the object into a dict
will_modify_config_cpu_requirements_dict = will_modify_config_cpu_requirements_instance.to_dict()
# create an instance of WillModifyConfigCpuRequirements from a dict
will_modify_config_cpu_requirements_form_dict = will_modify_config_cpu_requirements.from_dict(will_modify_config_cpu_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


