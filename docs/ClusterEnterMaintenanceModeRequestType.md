# ClusterEnterMaintenanceModeRequestType

The parameters of *ClusterComputeResource.ClusterEnterMaintenanceMode*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | The array of hosts to put into maintenance mode.  ***Required privileges:*** Host.Config.Maintenance  Refers instances of *HostSystem*.  | 
**option** | [**List[OptionValue]**](OptionValue.md) | An array of *OptionValue* options for this query. The specified options override the advanced options in *ClusterDrsConfigInfo*.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_enter_maintenance_mode_request_type import ClusterEnterMaintenanceModeRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEnterMaintenanceModeRequestType from a JSON string
cluster_enter_maintenance_mode_request_type_instance = ClusterEnterMaintenanceModeRequestType.from_json(json)
# print the JSON string representation of the object
print ClusterEnterMaintenanceModeRequestType.to_json()

# convert the object into a dict
cluster_enter_maintenance_mode_request_type_dict = cluster_enter_maintenance_mode_request_type_instance.to_dict()
# create an instance of ClusterEnterMaintenanceModeRequestType from a dict
cluster_enter_maintenance_mode_request_type_form_dict = cluster_enter_maintenance_mode_request_type.from_dict(cluster_enter_maintenance_mode_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


