# ResolveInstallationErrorsOnClusterRequestType

The parameters of *IoFilterManager.ResolveInstallationErrorsOnCluster_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_id** | **str** | ID of the filter.  | 
**cluster** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.resolve_installation_errors_on_cluster_request_type import ResolveInstallationErrorsOnClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ResolveInstallationErrorsOnClusterRequestType from a JSON string
resolve_installation_errors_on_cluster_request_type_instance = ResolveInstallationErrorsOnClusterRequestType.from_json(json)
# print the JSON string representation of the object
print ResolveInstallationErrorsOnClusterRequestType.to_json()

# convert the object into a dict
resolve_installation_errors_on_cluster_request_type_dict = resolve_installation_errors_on_cluster_request_type_instance.to_dict()
# create an instance of ResolveInstallationErrorsOnClusterRequestType from a dict
resolve_installation_errors_on_cluster_request_type_form_dict = resolve_installation_errors_on_cluster_request_type.from_dict(resolve_installation_errors_on_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


