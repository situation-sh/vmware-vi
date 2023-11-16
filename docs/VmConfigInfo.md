# VmConfigInfo

VM Configuration.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**List[VAppProductInfo]**](VAppProductInfo.md) | Information about the package content.  ***Since:*** vSphere API 4.0  | [optional] 
**var_property** | [**List[VAppPropertyInfo]**](VAppPropertyInfo.md) | List of properties  ***Since:*** vSphere API 4.0  | [optional] 
**ip_assignment** | [**VAppIPAssignmentInfo**](VAppIPAssignmentInfo.md) |  | 
**eula** | **List[str]** | End User Liceses Agreements.  ***Since:*** vSphere API 4.0  | [optional] 
**ovf_section** | [**List[VAppOvfSectionInfo]**](VAppOvfSectionInfo.md) | List of uninterpreted OVF meta-data sections.  ***Since:*** vSphere API 4.0  | [optional] 
**ovf_environment_transport** | **List[str]** | List the transports to use for properties.  Supported values are: iso and com.vmware.guestInfo.  ***Since:*** vSphere API 4.0  | [optional] 
**install_boot_required** | **bool** | Specifies whether the VM needs an initial boot before the deployment is complete.  Not relevant for vApps. This means that the value is always false when reading the configuration and is ignored when setting the configuration.  If a vApp requires an install boot (because one of its VMs does), this is visible on the *VirtualAppSummary.installBootRequired* field of the vApp.  ***Since:*** vSphere API 4.0  | 
**install_boot_stop_delay** | **int** | Specifies the delay in seconds to wait for the VM to power off after the initial boot (used only if installBootRequired is true).  A value of 0 means wait forever.  Not relevant for vApps. This means that the value is always false when reading the configuration and is ignored when setting the configuration.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.vm_config_info import VmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of VmConfigInfo from a JSON string
vm_config_info_instance = VmConfigInfo.from_json(json)
# print the JSON string representation of the object
print VmConfigInfo.to_json()

# convert the object into a dict
vm_config_info_dict = vm_config_info_instance.to_dict()
# create an instance of VmConfigInfo from a dict
vm_config_info_form_dict = vm_config_info.from_dict(vm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


