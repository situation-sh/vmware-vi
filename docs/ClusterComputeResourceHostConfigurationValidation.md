# ClusterComputeResourceHostConfigurationValidation

Describes the validations applicable to the settings on the host.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**is_dvs_setting_valid** | **bool** | Check if the host is attached to the DVS on right adapters.  ***Since:*** vSphere API 6.7.1  | [optional] 
**is_vmknic_setting_valid** | **bool** | Check if the adapters for services are present and on the right portgroups.  ***Since:*** vSphere API 6.7.1  | [optional] 
**is_ntp_setting_valid** | **bool** | Check if NTP is configured per specification.  ***Since:*** vSphere API 6.7.1  | [optional] 
**is_lockdown_mode_valid** | **bool** | Check if lockdown mode is set per specification  ***Since:*** vSphere API 6.7.1  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_host_configuration_validation import ClusterComputeResourceHostConfigurationValidation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceHostConfigurationValidation from a JSON string
cluster_compute_resource_host_configuration_validation_instance = ClusterComputeResourceHostConfigurationValidation.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceHostConfigurationValidation.to_json()

# convert the object into a dict
cluster_compute_resource_host_configuration_validation_dict = cluster_compute_resource_host_configuration_validation_instance.to_dict()
# create an instance of ClusterComputeResourceHostConfigurationValidation from a dict
cluster_compute_resource_host_configuration_validation_form_dict = cluster_compute_resource_host_configuration_validation.from_dict(cluster_compute_resource_host_configuration_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


