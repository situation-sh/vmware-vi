# HostRuntimeInfo

This data object type describes the runtime state of a host. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_state** | [**HostSystemConnectionStateEnum**](HostSystemConnectionStateEnum.md) |  | 
**power_state** | [**HostSystemPowerStateEnum**](HostSystemPowerStateEnum.md) |  | 
**standby_mode** | **str** | The host&#39;s standby mode.  For valid values see *HostStandbyMode_enum*. The property is only populated by vCenter server. If queried directly from a ESX host, the property is is unset.  ***Since:*** vSphere API 4.1  | [optional] 
**in_maintenance_mode** | **bool** | The flag to indicate whether or not the host is in maintenance mode.  This flag is set when the host has entered the maintenance mode. It is not set during the entering phase of maintenance mode.  See also *HostSystem.EnterMaintenanceMode_Task*, *HostSystem.ExitMaintenanceMode_Task*.  | 
**in_quarantine_mode** | **bool** | The flag to indicate whether or not the host is in quarantine mode.  InfraUpdateHa will recommend to set this flag based on the HealthUpdates received by the HealthUpdateProviders configured for the cluster. A host that is reported as degraded will be recommended to enter quarantine mode, while a host that is reported as healthy will be recommended to exit quarantine mode. Execution of these recommended actions will set this flag. Hosts in quarantine mode will be avoided by vSphere DRS as long as the increased consolidation in the cluster does not negatively affect VM performance.  See also *HealthUpdateManager*, *ClusterInfraUpdateHaConfigInfo*, *ClusterHostInfraUpdateHaModeAction*.  ***Since:*** vSphere API 6.5  | [optional] 
**boot_time** | **datetime** | The time when the host was booted.  | [optional] 
**health_system_runtime** | [**HealthSystemRuntime**](HealthSystemRuntime.md) |  | [optional] 
**das_host_state** | [**ClusterDasFdmHostState**](ClusterDasFdmHostState.md) |  | [optional] 
**tpm_pcr_values** | [**List[HostTpmDigestInfo]**](HostTpmDigestInfo.md) | Deprecated as of @released(\&quot;5.1\&quot;) this information should be considered to be neither complete nor reliable.  The array of PCR digest values stored in the TPM device since the last host boot time.  ***Since:*** vSphere API 4.0  | [optional] 
**vsan_runtime_info** | [**VsanHostRuntimeInfo**](VsanHostRuntimeInfo.md) |  | [optional] 
**network_runtime_info** | [**HostRuntimeInfoNetworkRuntimeInfo**](HostRuntimeInfoNetworkRuntimeInfo.md) |  | [optional] 
**v_flash_resource_runtime_info** | [**HostVFlashManagerVFlashResourceRunTimeInfo**](HostVFlashManagerVFlashResourceRunTimeInfo.md) |  | [optional] 
**host_max_virtual_disk_capacity** | **int** | The maximum theoretical virtual disk capacity supported by this host  ***Since:*** vSphere API 5.5  | [optional] 
**crypto_state** | **str** | Encryption state of the host.  Valid values are enumerated by the *CryptoState* type.  ***Since:*** vSphere API 6.5  | [optional] 
**crypto_key_id** | [**CryptoKeyId**](CryptoKeyId.md) |  | [optional] 
**stateless_nvds_migration_ready** | **str** | Indicating the host is ready for NVDS to VDS migration.  See *HostRuntimeInfoStatelessNvdsMigrationState_enum* for supported values.  ***Since:*** vSphere API 7.0.2.0  | [optional] 
**state_encryption** | [**HostRuntimeInfoStateEncryptionInfo**](HostRuntimeInfoStateEncryptionInfo.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_runtime_info import HostRuntimeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostRuntimeInfo from a JSON string
host_runtime_info_instance = HostRuntimeInfo.from_json(json)
# print the JSON string representation of the object
print HostRuntimeInfo.to_json()

# convert the object into a dict
host_runtime_info_dict = host_runtime_info_instance.to_dict()
# create an instance of HostRuntimeInfo from a dict
host_runtime_info_form_dict = host_runtime_info.from_dict(host_runtime_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


