# ClusterDpmConfigInfo

Configuration of the VMware DPM service.  All fields are defined as optional. In case of a reconfiguration, unset fields are not changed.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Flag indicating whether or not the service is enabled.  This service can not be enabled, unless DRS is enabled as well.  ***Since:*** VI API 2.5  | [optional] 
**default_dpm_behavior** | [**DpmBehaviorEnum**](DpmBehaviorEnum.md) |  | [optional] 
**host_power_action_rate** | **int** | DPM generates only those recommendations that are above the specified rating.  Ratings vary from 1 to 5. This setting applies to both manual and automated (@link DpmBehavior) DPM clusters.  ***Since:*** vSphere API 4.0  | [optional] 
**option** | [**List[OptionValue]**](OptionValue.md) | Deprecated as of vSphere API 4.1, use *ClusterDrsConfigInfo.option*.  Advanced settings.  ***Since:*** VI API 2.5  | [optional] 

## Example

```python
from vmware_vi.models.cluster_dpm_config_info import ClusterDpmConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDpmConfigInfo from a JSON string
cluster_dpm_config_info_instance = ClusterDpmConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDpmConfigInfo.to_json()

# convert the object into a dict
cluster_dpm_config_info_dict = cluster_dpm_config_info_instance.to_dict()
# create an instance of ClusterDpmConfigInfo from a dict
cluster_dpm_config_info_form_dict = cluster_dpm_config_info.from_dict(cluster_dpm_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


