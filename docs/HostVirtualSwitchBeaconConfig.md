# HostVirtualSwitchBeaconConfig

This data object type describes the configuration of the beacon to probe connectivity of physical network adapters.  A beacon is sent out of one network adapter and should arrive on another network adapter in the team. The successful roundtrip indicates that the network adapters are working.  Define this data object to enable beacon probing as a method to validate the link status of a physical network adapter. Beacon probing must be configured in order to use the beacon status as a criteria to determine if a physical network adapter failed.  See also *HostNicFailureCriteria.checkBeacon*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **int** | Determines how often, in seconds, a beacon should be sent.  | 

## Example

```python
from vmware_vi.models.host_virtual_switch_beacon_config import HostVirtualSwitchBeaconConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostVirtualSwitchBeaconConfig from a JSON string
host_virtual_switch_beacon_config_instance = HostVirtualSwitchBeaconConfig.from_json(json)
# print the JSON string representation of the object
print HostVirtualSwitchBeaconConfig.to_json()

# convert the object into a dict
host_virtual_switch_beacon_config_dict = host_virtual_switch_beacon_config_instance.to_dict()
# create an instance of HostVirtualSwitchBeaconConfig from a dict
host_virtual_switch_beacon_config_form_dict = host_virtual_switch_beacon_config.from_dict(host_virtual_switch_beacon_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


