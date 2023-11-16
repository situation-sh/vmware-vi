# ClusterComputeResourceHostConfigurationProfile

HostConfigurationProfile describes the configuration of services and settings which gets applied on every host in the HCI cluster.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_time_config** | [**HostDateTimeConfig**](HostDateTimeConfig.md) |  | [optional] 
**lockdown_mode** | [**HostLockdownModeEnum**](HostLockdownModeEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_compute_resource_host_configuration_profile import ClusterComputeResourceHostConfigurationProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceHostConfigurationProfile from a JSON string
cluster_compute_resource_host_configuration_profile_instance = ClusterComputeResourceHostConfigurationProfile.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceHostConfigurationProfile.to_json()

# convert the object into a dict
cluster_compute_resource_host_configuration_profile_dict = cluster_compute_resource_host_configuration_profile_instance.to_dict()
# create an instance of ClusterComputeResourceHostConfigurationProfile from a dict
cluster_compute_resource_host_configuration_profile_form_dict = cluster_compute_resource_host_configuration_profile.from_dict(cluster_compute_resource_host_configuration_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


