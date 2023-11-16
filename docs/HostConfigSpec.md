# HostConfigSpec

The *HostConfigSpec* data object provides access to data objects that specify configuration changes to be applied to an ESX host.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas_datastore** | [**List[HostNasVolumeConfig]**](HostNasVolumeConfig.md) | Configurations to create NAS datastores.  ***Since:*** vSphere API 4.0  | [optional] 
**network** | [**HostNetworkConfig**](HostNetworkConfig.md) |  | [optional] 
**nic_type_selection** | [**List[HostVirtualNicManagerNicTypeSelection]**](HostVirtualNicManagerNicTypeSelection.md) | Type selection for different VirtualNics.  ***Since:*** vSphere API 4.0  | [optional] 
**service** | [**List[HostServiceConfig]**](HostServiceConfig.md) | Host service configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**firewall** | [**HostFirewallConfig**](HostFirewallConfig.md) |  | [optional] 
**option** | [**List[OptionValue]**](OptionValue.md) | Host configuration options as defined by the *OptionValue* data object type.  ***Since:*** vSphere API 4.0  | [optional] 
**datastore_principal** | **str** | Datastore principal user.  ***Since:*** vSphere API 4.0  | [optional] 
**datastore_principal_passwd** | **str** | Password for the datastore principal.  ***Since:*** vSphere API 4.0  | [optional] 
**datetime** | [**HostDateTimeConfig**](HostDateTimeConfig.md) |  | [optional] 
**storage_device** | [**HostStorageDeviceInfo**](HostStorageDeviceInfo.md) |  | [optional] 
**license** | [**HostLicenseSpec**](HostLicenseSpec.md) |  | [optional] 
**security** | [**HostSecuritySpec**](HostSecuritySpec.md) |  | [optional] 
**user_account** | [**List[HostAccountSpec]**](HostAccountSpec.md) | List of users to create/update with new password.  ***Since:*** vSphere API 4.0  | [optional] 
**usergroup_account** | [**List[HostAccountSpec]**](HostAccountSpec.md) | List of users to create/update with new password.  ***Since:*** vSphere API 4.0  | [optional] 
**memory** | [**HostMemorySpec**](HostMemorySpec.md) |  | [optional] 
**active_directory** | [**List[HostActiveDirectory]**](HostActiveDirectory.md) | Active Directory configuration change.  ***Since:*** vSphere API 4.1  | [optional] 
**generic_config** | [**List[KeyAnyValue]**](KeyAnyValue.md) | Advanced configuration.  ***Since:*** vSphere API 5.0  | [optional] 
**graphics_config** | [**HostGraphicsConfig**](HostGraphicsConfig.md) |  | [optional] 
**assignable_hardware_config** | [**HostAssignableHardwareConfig**](HostAssignableHardwareConfig.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_config_spec import HostConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigSpec from a JSON string
host_config_spec_instance = HostConfigSpec.from_json(json)
# print the JSON string representation of the object
print HostConfigSpec.to_json()

# convert the object into a dict
host_config_spec_dict = host_config_spec_instance.to_dict()
# create an instance of HostConfigSpec from a dict
host_config_spec_form_dict = host_config_spec.from_dict(host_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


