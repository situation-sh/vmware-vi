# DistributedVirtualPortgroupInfo

This class describes a DistributedVirtualPortgroup that a device backing can be attached to.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**switch_name** | **str** | The name of the switch.  ***Since:*** vSphere API 4.0  | 
**switch_uuid** | **str** | The UUID of the switch.  ***Since:*** vSphere API 4.0  | 
**portgroup_name** | **str** | The name of the portgroup.  ***Since:*** vSphere API 4.0  | 
**portgroup_key** | **str** | The key of the portgroup.  ***Since:*** vSphere API 4.0  | 
**portgroup_type** | **str** | The type of portgroup.  See *DistributedVirtualPortgroupPortgroupType_enum*  ***Since:*** vSphere API 4.0  | 
**uplink_portgroup** | **bool** | Whether this portgroup is an uplink portgroup.  ***Since:*** vSphere API 4.0  | 
**portgroup** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**network_reservation_supported** | **bool** | Indicates whether network bandwidth reservation is supported on the portgroup  ***Since:*** vSphere API 6.0  | [optional] 
**backing_type** | **str** | Backing type of portgroup.  See *DistributedVirtualPortgroup*.*DistributedVirtualPortgroupBackingType_enum* for possible values. The default value is \&quot;standard\&quot;.  ***Since:*** vSphere API 7.0  | [optional] 
**logical_switch_uuid** | **str** | The logical switch UUID, which is used by NSX portgroup  ***Since:*** vSphere API 7.0  | [optional] 
**segment_id** | **str** | The segment ID of logical switch, which is used by NSX portroup  ***Since:*** vSphere API 7.0  | [optional] 

## Example

```python
from vmware_vi.models.distributed_virtual_portgroup_info import DistributedVirtualPortgroupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualPortgroupInfo from a JSON string
distributed_virtual_portgroup_info_instance = DistributedVirtualPortgroupInfo.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualPortgroupInfo.to_json()

# convert the object into a dict
distributed_virtual_portgroup_info_dict = distributed_virtual_portgroup_info_instance.to_dict()
# create an instance of DistributedVirtualPortgroupInfo from a dict
distributed_virtual_portgroup_info_form_dict = distributed_virtual_portgroup_info.from_dict(distributed_virtual_portgroup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


