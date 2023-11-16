# ClusterDrsConfigInfo

The *ClusterDrsConfigInfo* data object contains configuration information for the VMware DRS service.  All fields are optional. If you set the <code>modify</code> parameter to <code>true</code> when you call *ComputeResource.ReconfigureComputeResource_Task*, an unset property has no effect on the existing property value in the cluster configuration on the Server. If you set the <code>modify</code> parameter to <code>false</code> when you reconfigure a cluster, the cluster configuration is reverted to the default values, then the new configuration values are applied. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Deprecated as of vSphere API 7.0. To disable DRS load balancing, please use the lowest DRS aggressiveness level, setting *ClusterDrsConfigInfo.vmotionRate* to 5, and/or setting *ClusterDrsConfigInfo.defaultVmBehavior* to manual. The former only generates manadatory move recommendations, not load balancing recommendations. The latter only generates recommendations, without executing them. To remove all the child resource pools, please find the root resource pool *ComputeResource.resourcePool*, and destroy all its children *ResourcePool.DestroyChildren*. Vice versa.  Flag indicating whether or not DRS service is enabled.  | [optional] 
**enable_vm_behavior_overrides** | **bool** | Flag that dictates whether DRS Behavior overrides for individual virtual machines (*ClusterDrsVmConfigInfo*) are enabled.  The default value is &lt;code&gt;true&lt;/code&gt;.  When this flag is &lt;code&gt;true&lt;/code&gt;, the *ClusterConfigSpecEx*.*ClusterConfigSpecEx.drsVmConfigSpec* values override the *ClusterDrsConfigInfo.defaultVmBehavior*.  When this flag is &lt;code&gt;false&lt;/code&gt;, the *ClusterDrsConfigInfo.defaultVmBehavior* value applies to all virtual machines, with the following exception: in a cluster that has EVC disabled, you cannot override the virtual machine setting (*ClusterConfigSpecEx.drsVmConfigSpec*) for Fault Tolerance virtual machines.  ***Since:*** vSphere API 4.0  | [optional] 
**default_vm_behavior** | [**DrsBehaviorEnum**](DrsBehaviorEnum.md) |  | [optional] 
**vmotion_rate** | **int** | Threshold for generated *ClusterRecommendation*s.  DRS generates only those recommendations that are above the specified vmotionRate. Ratings vary from 1 to 5. This setting applies to manual, partiallyAutomated, and fullyAutomated DRS clusters. See *DrsBehavior_enum*.  | [optional] 
**scale_descendants_shares** | **str** | Specifies the scaling behavior of the shares of all resource pools in the cluster.  See *ResourceConfigSpecScaleSharesBehavior_enum* for possible values. If any scaling behavior other than *disabled* is specified, the system will scale the CPU and memory shares allocated to each resource pool with the total shares of all powered on virtual machines under each respective pool. The system will also use the *SharesInfo* set on each resource pool as a multiplier for the scale. Setting the *ClusterDrsConfigInfo.scaleDescendantsShares* on the cluster is equivalent to setting the *ResourceConfigSpec.scaleDescendantsShares* on the root resource pool.  ***Since:*** vSphere API 7.0  | [optional] 
**option** | [**List[OptionValue]**](OptionValue.md) | Advanced settings.  | [optional] 

## Example

```python
from vmware_vi.models.cluster_drs_config_info import ClusterDrsConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterDrsConfigInfo from a JSON string
cluster_drs_config_info_instance = ClusterDrsConfigInfo.from_json(json)
# print the JSON string representation of the object
print ClusterDrsConfigInfo.to_json()

# convert the object into a dict
cluster_drs_config_info_dict = cluster_drs_config_info_instance.to_dict()
# create an instance of ClusterDrsConfigInfo from a dict
cluster_drs_config_info_form_dict = cluster_drs_config_info.from_dict(cluster_drs_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


