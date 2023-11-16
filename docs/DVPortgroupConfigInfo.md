# DVPortgroupConfigInfo

The *DVPortgroupConfigInfo* data object defines the configuration of a *DistributedVirtualPortgroup*.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Key of the portgroup.  ***Since:*** vSphere API 4.0  | 
**name** | **str** | Name of the portgroup.  ***Since:*** vSphere API 4.0  | 
**num_ports** | **int** | Number of ports in the portgroup.  ***Since:*** vSphere API 4.0  | 
**distributed_virtual_switch** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**default_port_config** | [**DVPortSetting**](DVPortSetting.md) |  | [optional] 
**description** | **str** | Description of the portgroup.  ***Since:*** vSphere API 4.0  | [optional] 
**type** | **str** | Type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupPortgroupType_enum* for possible values.  ***Since:*** vSphere API 4.0  | 
**backing_type** | **str** | Backing type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupBackingType_enum* for possible values. The default value is \&quot;standard\&quot;  ***Since:*** vSphere API 7.0  | [optional] 
**policy** | [**DVPortgroupPolicy**](DVPortgroupPolicy.md) |  | 
**port_name_format** | **str** | If set, a name will be automatically generated based on this format string for a port when it is created in or moved into the portgroup.  The format string can contain meta tags that will be resolved to the corresponding values in generating a name, if applicable for the port at the time of name generation.  To insert a meta tag in the format string, enclose the names defined as meta tag names inside angle brackets. See *DistributedVirtualPortgroupMetaTagName_enum* for a list of currently available meta tags. For example, \&quot;redNetwork-&amp;lt;portIndex&amp;gt;\&quot; and \&quot;&amp;lt;dvsName&amp;gt;-pnic&amp;lt;portIndex&amp;gt;\&quot; result in generated port names like \&quot;redNetwork-2\&quot; and \&quot;switch-pnic3\&quot;.  If a meta tag is recognized, but there is no applicable value, the tag will be expanded to empty string. If an arbitrary name appears inside a \&quot;&amp;lt;&amp;gt;\&quot; pair and is not recognized as one of the defined meta tags, the substring is treated as-is and appear unchanged in the generated name.  To prevent a meta tag from being expanded, prefix the meta tag with a &#39;\\\\&#39; (backslash). For example, the format string \&quot;abc\\\\&amp;lt;portIndex&amp;gt;def\&quot; results in the generated port name \&quot;abc&amp;lt;portIndex&amp;gt;def\&quot;.  ***Since:*** vSphere API 4.0  | [optional] 
**scope** | [**List[ManagedObjectReference]**](ManagedObjectReference.md) | Deprecated as of vSphere API 5.5.  Eligible entities that can connect to the portgroup.  If unset, there is no restriction on which entity can connect to the portgroup. If set, only the entities in the specified list or their child entities are allowed to connect to the portgroup. If scopes are defined at both port and portgroup level, they are taken as an \&quot;AND\&quot; relationship. If such a relationship doesn&#39;t make sense, the reconfigure operation will raise an exception.  ***Since:*** vSphere API 4.0  Refers instances of *ManagedEntity*.  | [optional] 
**vendor_specific_config** | [**List[DistributedVirtualSwitchKeyedOpaqueBlob]**](DistributedVirtualSwitchKeyedOpaqueBlob.md) | Opaque binary blob that stores vendor specific configuration.  ***Since:*** vSphere API 4.0  | [optional] 
**config_version** | **str** | Configuration version number.  ***Since:*** vSphere API 4.0  | [optional] 
**auto_expand** | **bool** | If set to true, this property ignores the limit on the number of ports in the portgroup.  When a Virtual Machine/Host tries to connect to the portgroup and there are no free ports available in the portgroup, new ports will be automatically added to the portgroup. The flag is currently supported only for static portgroups.  When this property is set to true, the portgroup becomes a potential candidate for auto-shrink. Once the portgroup has auto-expanded then its disconnected ports are likely to be deleted automatically, as a part of auto-shrink step, if there are more than certain number of free ports. If the portgroup never auto-expanded, then it will never lose any free ports.  ***Since:*** vSphere API 5.0  | [optional] 
**vm_vnic_network_resource_pool_key** | **str** | The key of virtual NIC network resource pool to be associated with a portgroup.  The default value for this property is unset, indicating that this portgroup is not associated with any virtual NIC network resource pool. To clear the value of this property and revert to unset, set the *DVPortgroupConfigSpec.vmVnicNetworkResourcePoolKey* to \&quot;-1\&quot; in an update operation.  ***Since:*** vSphere API 6.0  | [optional] 
**uplink** | **bool** | Indicates whether the portgroup is an uplink portroup.  ***Since:*** vSphere API 6.5  | [optional] 
**transport_zone_uuid** | **str** | The UUID of transport zone to be associated with a NSX portgroup.  ***Since:*** vSphere API 7.0  | [optional] 
**transport_zone_name** | **str** | The name of transport zone to be associated with a NSX portgroup.  ***Since:*** vSphere API 7.0  | [optional] 
**logical_switch_uuid** | **str** | The logical switch UUID, which is used by NSX portgroup  ***Since:*** vSphere API 7.0  | [optional] 
**segment_id** | **str** | The segment ID of logical switch  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.dv_portgroup_config_info import DVPortgroupConfigInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DVPortgroupConfigInfo from a JSON string
dv_portgroup_config_info_instance = DVPortgroupConfigInfo.from_json(json)
# print the JSON string representation of the object
print DVPortgroupConfigInfo.to_json()

# convert the object into a dict
dv_portgroup_config_info_dict = dv_portgroup_config_info_instance.to_dict()
# create an instance of DVPortgroupConfigInfo from a dict
dv_portgroup_config_info_form_dict = dv_portgroup_config_info.from_dict(dv_portgroup_config_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


