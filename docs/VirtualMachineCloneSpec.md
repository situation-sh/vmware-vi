# VirtualMachineCloneSpec

Specification for a virtual machine cloning operation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**VirtualMachineRelocateSpec**](VirtualMachineRelocateSpec.md) |  | 
**template** | **bool** | Specifies whether or not the new virtual machine should be marked as a template.  | 
**config** | [**VirtualMachineConfigSpec**](VirtualMachineConfigSpec.md) |  | [optional] 
**customization** | [**CustomizationSpec**](CustomizationSpec.md) |  | [optional] 
**power_on** | **bool** | Specifies whether or not the new VirtualMachine should be powered on after creation.  As part of a customization, this flag is normally set to true, since the first power-on operation completes the customization process. This flag is ignored if a template is being created.  | 
**snapshot** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**memory** | **bool** | Flag indicating whether to retain a copy of the source virtual machine&#39;s memory state in the clone.  Retaining the memory state during clone results in a clone in suspended state with all network adapters removed to avoid network conflicts, except those with a VirtualEthernetCard.addressType of \&quot;manual\&quot;. Users of this flag should take special care so that, when adding a network adapter back to the clone, the VM is not resumed on the same VM network as the source VM, or else MAC address conflicts could occur. When cloning between two hosts with different CPUs outside an EVC cluster, users of this flag should be aware that vCenter does not verify CPU compatibility between the clone&#39;s memory state and the target host prior to the clone operation, so the clone may fail to resume until it is migrated to a host with a compatible CPU.  This flag is ignored if the snapshot parameter is unset. This flag only applies for a snapshot taken on a running or suspended virtual machine with the &#39;memory&#39; parameter set to true, because otherwise the snapshot has no memory state. This flag defaults to false.  ***Since:*** vSphere API 5.5  | [optional] 
**tpm_provision_policy** | **str** | Provisioning policy for virtual TPM devices during VM clone operations.  The list of supported values is defined in *VirtualMachineCloneSpecTpmProvisionPolicy_enum*.  If unset - a globally defined policy is used, which by default is set to &#39;copy&#39;.  | [optional] 

## Example

```python
from vmware_vi.models.virtual_machine_clone_spec import VirtualMachineCloneSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineCloneSpec from a JSON string
virtual_machine_clone_spec_instance = VirtualMachineCloneSpec.from_json(json)
# print the JSON string representation of the object
print VirtualMachineCloneSpec.to_json()

# convert the object into a dict
virtual_machine_clone_spec_dict = virtual_machine_clone_spec_instance.to_dict()
# create an instance of VirtualMachineCloneSpec from a dict
virtual_machine_clone_spec_form_dict = virtual_machine_clone_spec.from_dict(virtual_machine_clone_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


