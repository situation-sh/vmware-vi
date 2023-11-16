# ServiceContent

The *ServiceContent* data object defines properties for the ServiceInstance managed object.  The ServiceInstance itself does not have directly-accessible properties because reading the properties of a managed object requires the use of a property collector, and the property collector itself is a property of the *ServiceInstance*. For this reason, use the method *ServiceInstance.RetrieveServiceContent* to retrieve the *ServiceContent* object. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**property_collector** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**view_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**about** | [**AboutInfo**](AboutInfo.md) |  | 
**setting** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**user_directory** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**session_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**authorization_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**service_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**perf_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**scheduled_task_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**alarm_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**event_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**task_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**extension_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**customization_spec_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**guest_customization_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**custom_fields_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**account_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**diagnostic_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**license_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**search_index** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**file_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**datastore_namespace_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**virtual_disk_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**virtualization_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**snmp_system** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**vm_provisioning_checker** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**vm_compatibility_checker** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**ovf_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**ip_pool_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**dv_switch_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host_profile_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**cluster_profile_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**compliance_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**localization_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**storage_resource_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**guest_operations_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**overhead_memory_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**certificate_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**io_filter_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**v_storage_object_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host_spec_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**crypto_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**health_update_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**failover_cluster_configurator** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**failover_cluster_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**tenant_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**site_info_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**storage_query_manager** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.service_content import ServiceContent

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceContent from a JSON string
service_content_instance = ServiceContent.from_json(json)
# print the JSON string representation of the object
print ServiceContent.to_json()

# convert the object into a dict
service_content_dict = service_content_instance.to_dict()
# create an instance of ServiceContent from a dict
service_content_form_dict = service_content.from_dict(service_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


