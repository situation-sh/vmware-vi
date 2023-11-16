# ClusterDpmHostConfigInfo

DPM configuration for a single host.  This makes it possible to override the default behavior for an individual host.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**enabled** | **bool** | Flag to indicate whether or not VirtualCenter is allowed to perform any power related operations or recommendations for this host.  If this flag is false, the host is effectively excluded from DPM service.  If no individual DPM specification exists for a host, this property defaults to true.  ***Since:*** VI API 2.5  | [optional] 
**behavior** | [**DpmBehaviorEnum**](DpmBehaviorEnum.md) |  | [optional] 

## Example

```python
from vmware_vi.models.cluster_dpm_host_config_info import ClusterDpmHostConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDpmHostConfigInfo from a JSON string
cluster_dpm_host_config_info_instance = ClusterDpmHostConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDpmHostConfigInfo.to_json()

# convert the object into a dict
cluster_dpm_host_config_info_dict = cluster_dpm_host_config_info_instance.to_dict()
# create an instance of ClusterDpmHostConfigInfo from a dict
cluster_dpm_host_config_info_form_dict = cluster_dpm_host_config_info.from_dict(cluster_dpm_host_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


