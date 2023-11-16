# ArrayOfVsanHostClusterStatus

A boxed array of *VsanHostClusterStatus*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VsanHostClusterStatus]**](VsanHostClusterStatus.md) |  | 

## Example

```python
from vmware_vi.models.array_of_vsan_host_cluster_status import ArrayOfVsanHostClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVsanHostClusterStatus from a JSON string
array_of_vsan_host_cluster_status_instance = ArrayOfVsanHostClusterStatus.from_json(json)
# print the JSON string representation of the object
print ArrayOfVsanHostClusterStatus.to_json()

# convert the object into a dict
array_of_vsan_host_cluster_status_dict = array_of_vsan_host_cluster_status_instance.to_dict()
# create an instance of ArrayOfVsanHostClusterStatus from a dict
array_of_vsan_host_cluster_status_form_dict = array_of_vsan_host_cluster_status.from_dict(array_of_vsan_host_cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


