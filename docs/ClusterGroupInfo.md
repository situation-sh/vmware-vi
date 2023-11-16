# ClusterGroupInfo

*ClusterGroupInfo* is the base type for all virtual machine and host groups.  All virtual machines and hosts that are part of a group must be part of the same cluster.  ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique name of the group.  ***Since:*** vSphere API 4.1  | 
**user_created** | **bool** | Flag to indicate whether the group is created by the user or the system.  ***Since:*** vSphere API 5.0  | [optional] 
**unique_id** | **str** | Unique ID for the group.  uniqueID is unique within a cluster. Groups residing in different clusters might share a uniqueID.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.cluster_group_info import ClusterGroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterGroupInfo from a JSON string
cluster_group_info_instance = ClusterGroupInfo.from_json(json)
# print the JSON string representation of the object
print ClusterGroupInfo.to_json()

# convert the object into a dict
cluster_group_info_dict = cluster_group_info_instance.to_dict()
# create an instance of ClusterGroupInfo from a dict
cluster_group_info_form_dict = cluster_group_info.from_dict(cluster_group_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


