# HostConfigManager

This data object type describes the configuration of a host across products and versions. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_scheduler** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**datastore_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**memory_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**storage_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**network_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**vmotion_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**virtual_nic_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**service_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**firewall_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**advanced_option** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**diagnostic_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**auto_start_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**snmp_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**date_time_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**patch_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**image_config_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**boot_device_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**firmware_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**health_status_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**pci_passthru_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**license_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**kernel_module_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**authentication_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**power_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**cache_configuration_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**esx_agent_host_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**iscsi_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**v_flash_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**vsan_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**message_bus_proxy** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**user_directory** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**account_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host_access_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**graphics_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**vsan_internal_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**certificate_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**crypto_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**nvdimm_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**assignable_hardware_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.host_config_manager import HostConfigManager

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigManager from a JSON string
host_config_manager_instance = HostConfigManager.from_json(json)
# print the JSON string representation of the object
print HostConfigManager.to_json()

# convert the object into a dict
host_config_manager_dict = host_config_manager_instance.to_dict()
# create an instance of HostConfigManager from a dict
host_config_manager_form_dict = host_config_manager.from_dict(host_config_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


