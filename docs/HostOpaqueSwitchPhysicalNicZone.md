# HostOpaqueSwitchPhysicalNicZone


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The zone ID  ***Since:*** vSphere API 6.0  | 
**pnic_device** | **List[str]** | Whenever an OpaqueSwitch is associated with a PhysicalNicZone, then by default, the zone will consist of all physical nics that are linked to the switch.  However, if this property is set, then the zone will be considered to be consisting of only those physical nics that are listed here.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.host_opaque_switch_physical_nic_zone import HostOpaqueSwitchPhysicalNicZone

# TODO update the JSON string below
json = "{}"
# create an instance of HostOpaqueSwitchPhysicalNicZone from a JSON string
host_opaque_switch_physical_nic_zone_instance = HostOpaqueSwitchPhysicalNicZone.from_json(json)
# print the JSON string representation of the object
print HostOpaqueSwitchPhysicalNicZone.to_json()

# convert the object into a dict
host_opaque_switch_physical_nic_zone_dict = host_opaque_switch_physical_nic_zone_instance.to_dict()
# create an instance of HostOpaqueSwitchPhysicalNicZone from a dict
host_opaque_switch_physical_nic_zone_form_dict = host_opaque_switch_physical_nic_zone.from_dict(host_opaque_switch_physical_nic_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


