# VirtualMachineCloneSpecTpmProvisionPolicy

A boxed *VirtualMachineCloneSpecTpmProvisionPolicy_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**VirtualMachineCloneSpecTpmProvisionPolicyEnum**](VirtualMachineCloneSpecTpmProvisionPolicyEnum.md) |  | 

## Example

```python
from vmware_vi.models.virtual_machine_clone_spec_tpm_provision_policy import VirtualMachineCloneSpecTpmProvisionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineCloneSpecTpmProvisionPolicy from a JSON string
virtual_machine_clone_spec_tpm_provision_policy_instance = VirtualMachineCloneSpecTpmProvisionPolicy.from_json(json)
# print the JSON string representation of the object
print VirtualMachineCloneSpecTpmProvisionPolicy.to_json()

# convert the object into a dict
virtual_machine_clone_spec_tpm_provision_policy_dict = virtual_machine_clone_spec_tpm_provision_policy_instance.to_dict()
# create an instance of VirtualMachineCloneSpecTpmProvisionPolicy from a dict
virtual_machine_clone_spec_tpm_provision_policy_form_dict = virtual_machine_clone_spec_tpm_provision_policy.from_dict(virtual_machine_clone_spec_tpm_provision_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


