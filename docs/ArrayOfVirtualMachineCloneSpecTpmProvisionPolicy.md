# ArrayOfVirtualMachineCloneSpecTpmProvisionPolicy

A boxed array of *VirtualMachineCloneSpecTpmProvisionPolicy_enum*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineCloneSpecTpmProvisionPolicyEnum]**](VirtualMachineCloneSpecTpmProvisionPolicyEnum.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_clone_spec_tpm_provision_policy import ArrayOfVirtualMachineCloneSpecTpmProvisionPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineCloneSpecTpmProvisionPolicy from a JSON string
array_of_virtual_machine_clone_spec_tpm_provision_policy_instance = ArrayOfVirtualMachineCloneSpecTpmProvisionPolicy.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineCloneSpecTpmProvisionPolicy.to_json()

# convert the object into a dict
array_of_virtual_machine_clone_spec_tpm_provision_policy_dict = array_of_virtual_machine_clone_spec_tpm_provision_policy_instance.to_dict()
# create an instance of ArrayOfVirtualMachineCloneSpecTpmProvisionPolicy from a dict
array_of_virtual_machine_clone_spec_tpm_provision_policy_form_dict = array_of_virtual_machine_clone_spec_tpm_provision_policy.from_dict(array_of_virtual_machine_clone_spec_tpm_provision_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


