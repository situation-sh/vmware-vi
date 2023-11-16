# BatchAddHostsToClusterRequestType

The parameters of *Folder.BatchAddHostsToCluster_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**new_hosts** | [**List[FolderNewHostSpec]**](FolderNewHostSpec.md) | Specifies a list of new hosts to be added to the cluster. Hosts are first added as standalone hosts.  ***Since:*** vSphere API 6.7.1  | [optional] 
**existing_hosts** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Specifies a list of existing hosts to be added to the cluster. Hosts are first moved to the desired state before moving them to cluster.  Refers instances of *HostSystem*.  | [optional] 
**comp_res_spec** | [**ComputeResourceConfigSpec**](ComputeResourceConfigSpec.md) |  | [optional] 
**desired_state** | **str** | Specifies desired state for hosts once added to the cluster. If not specified, hosts are added to the cluster in their current state. See *FolderDesiredHostState_enum* for valid values.  | [optional] 

## Example

```python
from vmware_vi.models.batch_add_hosts_to_cluster_request_type import BatchAddHostsToClusterRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of BatchAddHostsToClusterRequestType from a JSON string
batch_add_hosts_to_cluster_request_type_instance = BatchAddHostsToClusterRequestType.from_json(json)
# print the JSON string representation of the object
print BatchAddHostsToClusterRequestType.to_json()

# convert the object into a dict
batch_add_hosts_to_cluster_request_type_dict = batch_add_hosts_to_cluster_request_type_instance.to_dict()
# create an instance of BatchAddHostsToClusterRequestType from a dict
batch_add_hosts_to_cluster_request_type_form_dict = batch_add_hosts_to_cluster_request_type.from_dict(batch_add_hosts_to_cluster_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


