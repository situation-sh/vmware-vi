# ClusterSystemVMsConfigSpec

Configuration for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_datastores** | [**List[ClusterDatastoreUpdateSpec]**](ClusterDatastoreUpdateSpec.md) | The only datastores which can be used for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**not_allowed_datastores** | [**List[ClusterDatastoreUpdateSpec]**](ClusterDatastoreUpdateSpec.md) | Datastores which cannot be used for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0  | [optional] 
**ds_tag_categories_to_exclude** | [**List[ClusterTagCategoryUpdateSpec]**](ClusterTagCategoryUpdateSpec.md) | Tag categories identifying datastores, which cannot be used for System VMs deployment.  ***Since:*** vSphere API 7.0.3.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_system_vms_config_spec import ClusterSystemVMsConfigSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterSystemVMsConfigSpec from a JSON string
cluster_system_vms_config_spec_instance = ClusterSystemVMsConfigSpec.from_json(json)
# print the JSON string representation of the object
print ClusterSystemVMsConfigSpec.to_json()

# convert the object into a dict
cluster_system_vms_config_spec_dict = cluster_system_vms_config_spec_instance.to_dict()
# create an instance of ClusterSystemVMsConfigSpec from a dict
cluster_system_vms_config_spec_form_dict = cluster_system_vms_config_spec.from_dict(cluster_system_vms_config_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


