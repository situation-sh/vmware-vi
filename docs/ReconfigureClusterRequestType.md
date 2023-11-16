# ReconfigureClusterRequestType

The parameters of *ClusterComputeResource.ReconfigureCluster_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spec** | [**ClusterConfigSpec**](ClusterConfigSpec.md) |  | 
**modify** | **bool** | Flag to specify whether the specification (\&quot;spec\&quot;) should be applied incrementally. If \&quot;modify\&quot; is false and the operation succeeds, then the configuration of the cluster matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.  | 

## Example

```python
from vmware_vi.models.reconfigure_cluster_request_type import ReconfigureClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of ReconfigureClusterRequestType from a JSON string
reconfigure_cluster_request_type_instance = ReconfigureClusterRequestType.from_json(json)
# print the JSON string representation of the object
print ReconfigureClusterRequestType.to_json()

# convert the object into a dict
reconfigure_cluster_request_type_dict = reconfigure_cluster_request_type_instance.to_dict()
# create an instance of ReconfigureClusterRequestType from a dict
reconfigure_cluster_request_type_form_dict = reconfigure_cluster_request_type.from_dict(reconfigure_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


