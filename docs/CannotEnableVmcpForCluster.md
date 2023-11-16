# CannotEnableVmcpForCluster

This fault is thrown when an attempt is made to enable VM Component Protection on a cluster which contains a host that does not support this feature.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**host_name** | **str** | If set this reports the hostName.  This is used for printing the host name in the localized message as the host may have been removed from the vCenter&#39;s inventory by the time localization would be taking place.  ***Since:*** vSphere API 6.0  | [optional] 
**reason** | **str** | This reports the reason for host not meeting the requirements for enabling vSphere VMCP.  It can be the following reason. - APDTimeout disabled.    ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.cannot_enable_vmcp_for_cluster import CannotEnableVmcpForCluster

# TODO update the JSON string below
json = "{}"
# create an instance of CannotEnableVmcpForCluster from a JSON string
cannot_enable_vmcp_for_cluster_instance = CannotEnableVmcpForCluster.from_json(json)
# print the JSON string representation of the object
print CannotEnableVmcpForCluster.to_json()

# convert the object into a dict
cannot_enable_vmcp_for_cluster_dict = cannot_enable_vmcp_for_cluster_instance.to_dict()
# create an instance of CannotEnableVmcpForCluster from a dict
cannot_enable_vmcp_for_cluster_form_dict = cannot_enable_vmcp_for_cluster.from_dict(cannot_enable_vmcp_for_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


