# DistributedVirtualSwitchHostMemberTransportZoneInfo

Transport zone information.  ***Since:*** vSphere API 7.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The UUID of transport zone.  ***Since:*** vSphere API 7.0  | 
**type** | **str** | The type of transport zone.  See *DistributedVirtualSwitchHostMemberTransportZoneType_enum* for valid values.  ***Since:*** vSphere API 7.0  | 

## Example

```python
from vmware_vi.models.distributed_virtual_switch_host_member_transport_zone_info import DistributedVirtualSwitchHostMemberTransportZoneInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DistributedVirtualSwitchHostMemberTransportZoneInfo from a JSON string
distributed_virtual_switch_host_member_transport_zone_info_instance = DistributedVirtualSwitchHostMemberTransportZoneInfo.from_json(json)
# print the JSON string representation of the object
print DistributedVirtualSwitchHostMemberTransportZoneInfo.to_json()

# convert the object into a dict
distributed_virtual_switch_host_member_transport_zone_info_dict = distributed_virtual_switch_host_member_transport_zone_info_instance.to_dict()
# create an instance of DistributedVirtualSwitchHostMemberTransportZoneInfo from a dict
distributed_virtual_switch_host_member_transport_zone_info_form_dict = distributed_virtual_switch_host_member_transport_zone_info.from_dict(distributed_virtual_switch_host_member_transport_zone_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


