# ClusterComputeResourceDVSConfigurationValidation

Describes the validations applicable to the network settings.  These are based off the information recorded in *dvsSetting*.  ***Since:*** vSphere API 6.7.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_dvs_valid** | **bool** | Check if the DVS is alive.  ***Since:*** vSphere API 6.7.1  | 
**is_dvpg_valid** | **bool** | Check if the portgroups are valid.  ***Since:*** vSphere API 6.7.1  | 

## Example

```python
from vmware_vi.models.cluster_compute_resource_dvs_configuration_validation import ClusterComputeResourceDVSConfigurationValidation

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterComputeResourceDVSConfigurationValidation from a JSON string
cluster_compute_resource_dvs_configuration_validation_instance = ClusterComputeResourceDVSConfigurationValidation.from_json(json)
# print the JSON string representation of the object
print ClusterComputeResourceDVSConfigurationValidation.to_json()

# convert the object into a dict
cluster_compute_resource_dvs_configuration_validation_dict = cluster_compute_resource_dvs_configuration_validation_instance.to_dict()
# create an instance of ClusterComputeResourceDVSConfigurationValidation from a dict
cluster_compute_resource_dvs_configuration_validation_form_dict = cluster_compute_resource_dvs_configuration_validation.from_dict(cluster_compute_resource_dvs_configuration_validation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


