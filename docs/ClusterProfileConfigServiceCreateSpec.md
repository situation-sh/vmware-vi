# ClusterProfileConfigServiceCreateSpec

DataObject which allows reconfiguration of a profile based on services that will be available on the cluster.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **List[str]** | Type of the service for which the ClusterProfile is being requested.  If more than one service is specified, the created ClusterProfile will cater for all the services. Possible values are specified by *ClusterProfileServiceType_enum*. If unset, clear the compliance expressions on the profile.  ***Since:*** vSphere API 4.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_profile_config_service_create_spec import ClusterProfileConfigServiceCreateSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterProfileConfigServiceCreateSpec from a JSON string
cluster_profile_config_service_create_spec_instance = ClusterProfileConfigServiceCreateSpec.from_json(json)
# print the JSON string representation of the object
print ClusterProfileConfigServiceCreateSpec.to_json()

# convert the object into a dict
cluster_profile_config_service_create_spec_dict = cluster_profile_config_service_create_spec_instance.to_dict()
# create an instance of ClusterProfileConfigServiceCreateSpec from a dict
cluster_profile_config_service_create_spec_form_dict = cluster_profile_config_service_create_spec.from_dict(cluster_profile_config_service_create_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


