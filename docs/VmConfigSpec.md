# VmConfigSpec

vApp related configuration of a VM.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**List[VAppProductSpec]**](VAppProductSpec.md) | Information about the product.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**var_property** | [**List[VAppPropertySpec]**](VAppPropertySpec.md) | List of properties.  Adding and editing properties requires various privileges depending on which fields are affected. See *VAppPropertyInfo* for details.  Deleting properties requires the privilege VApp.ApplicationConfig.  ***Since:*** vSphere API 4.0  | [optional] 
**ip_assignment** | [**VAppIPAssignmentInfo**](VAppIPAssignmentInfo.md) |  | [optional] 
**eula** | **List[str]** | End User Liceses Agreements.  If this list is set, it replaces all exiting licenses. An empty list will not make any changes to installed licenses. A list with a single element {\&quot;\&quot;} will remove all licenses and leave an empty list.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**ovf_section** | [**List[VAppOvfSectionSpec]**](VAppOvfSectionSpec.md) | List of uninterpreted OVF meta-data sections.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**ovf_environment_transport** | **List[str]** | List the transports to use for properties.  Supported values are: iso and com.vmware.guestInfo.  If this list is set, it replaces all exiting entries. An empty list will not make any changes. A list with a single element {\&quot;\&quot;} will clear the list of transports.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**install_boot_required** | **bool** | If this is on a VirtualMachine object, it specifies whether the VM needs an initial boot before the deployment is complete.  If this is on a vApp object, it indicates than one or more VMs needs an initial reboot. This flag is automatically reset once the reboot has happened.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 
**install_boot_stop_delay** | **int** | Specifies the delay in seconds to wait for the VM to power off after the initial boot (used only if installBootRequired is true).  A value of 0 means wait forever.  Reconfigure privilege: VApp.ApplicationConfig  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.vm_config_spec import VmConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigSpec from a JSON string
vm_config_spec_instance = VmConfigSpec.from_json(json)
# print the JSON string representation of the object
print VmConfigSpec.to_json()

# convert the object into a dict
vm_config_spec_dict = vm_config_spec_instance.to_dict()
# create an instance of VmConfigSpec from a dict
vm_config_spec_form_dict = vm_config_spec.from_dict(vm_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


