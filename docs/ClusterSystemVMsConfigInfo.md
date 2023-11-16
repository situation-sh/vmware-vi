# ClusterSystemVMsConfigInfo

Configuration for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_datastores** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The only datastores which can be used for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0  Refers instances of *Datastore*.  | [optional] 
**not_allowed_datastores** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Datastores which cannot be used for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0  Refers instances of *Datastore*.  | [optional] 
**ds_tag_categories_to_exclude** | **List[str]** | Tag categories identifying datastores, which cannot be used for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_system_vms_config_info import ClusterSystemVMsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSystemVMsConfigInfo from a JSON string
cluster_system_vms_config_info_instance = ClusterSystemVMsConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterSystemVMsConfigInfo.to_json()

# convert the object into a dict
cluster_system_vms_config_info_dict = cluster_system_vms_config_info_instance.to_dict()
# create an instance of ClusterSystemVMsConfigInfo from a dict
cluster_system_vms_config_info_form_dict = cluster_system_vms_config_info.from_dict(cluster_system_vms_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


